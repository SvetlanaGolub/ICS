# Структура клиент-сервер для протокола OPC UA

Структура была реализована на языке Python с помощью библиотеки freeOPCUA. 
При запуске сервера есть возможность выбрать режим защищённого соединения с шифрованием и подписью или без.
Во время работы на стороне сервера каждые 2 секунды обновляются значения следующих параметров:
- Время
- Давление
- Температура

После подключения клиент считывает значения этих параметры аналогично раз в 2 секунды.
# Как использовать:
1. **Запуск сервера**
```
python3 OPCUA_server.py
```
Выбор режима соединения:
```
Use encryption and signature? y/n 
```
2. **Запуск клиента**
```
python3 OPCUA_client.py
```
Выбор режима соединения (должен соответствовать режиму, выбранному на стороне сервера):
```
Use encryption and signature? y/n 
```

# Трафик

С помощью ПО Wireshark были сделаны дампы трафика между клиентом и сервером.
1. Без шифрования - `opcua.pcapng`
2. С шифрованием и подписью - `opcua_with_enc.pcapng`