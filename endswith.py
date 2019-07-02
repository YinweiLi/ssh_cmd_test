a = b'\r\n\r\n\t*************************************************************\r\n\t*         FHN USP (R) Software for Fengine S5800            *\r\n\t*                                                           *\r\n\t*                    Version  V210R240                      *\r\n\t*                                                           *\r\n\t*  Copyright (c) 2000-2015 by FiberHome Networks Co., Ltd.  *\r\n\t*************************************************************\r\n\r\nBFJD-ISC3-M-S5852T-1#'
b = str(a)
if a and b.endswith('#'):
    print('yes')
else:
    print('no')