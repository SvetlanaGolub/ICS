/* Copyright (C) 2015-2017 Open Information Security Foundation
 *
 * You can copy, redistribute or modify this Program under the terms of
 * the GNU General Public License version 2 as published by the Free
 * Software Foundation.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * version 2 along with this program; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
 * 02110-1301, USA.
 */

/**
 * \file
 *
 * \author FirstName LastName <yourname@domain>
 */

#ifndef __DETECT_OPCUA_OPCUABUF_H__
#define __DETECT_OPCUA_OPCUABUF_H__

#include "app-layer-opcua.h"

typedef struct DetectOpcua_ {
    uint8_t             type;           /** < Opcua msg type to match */
    uint8_t             function;       /** < Opcua function to match */
    uint8_t             compare;        /** < Opcua compare word to match */
    uint8_t             size;           /** < Opcua packet size to match */
    uint8_t             prev_token;     /** < Opcua previous token to match */
    uint8_t             req;            /** < Opcua request id to match */

} DetectOpcua;

void DetectOPCUAopcuabufRegister(void);

#endif /* __DETECT_OPCUA_OPCUABUF_H__ */
