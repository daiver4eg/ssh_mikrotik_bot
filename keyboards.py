from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import list_arrays as arl
#menu width
mainMenu = InlineKeyboardMarkup(row_width=2)
#create a buttons
btn_tt_opc1 = InlineKeyboardButton(text=arl.opc_arr_1[0], callback_data=arl.opc_arr_1[1])
btn_tt_opc2 = InlineKeyboardButton(text=arl.opc_arr_2[0], callback_data=arl.opc_arr_2[1])
btn_tt_opc3 = InlineKeyboardButton(text=arl.opc_arr_3[0], callback_data=arl.opc_arr_3[1])
btn_tt_opc4 = InlineKeyboardButton(text=arl.opc_arr_4[0], callback_data=arl.opc_arr_4[1])
btn_tt_opc5 = InlineKeyboardButton(text=arl.opc_arr_5[0], callback_data=arl.opc_arr_5[1])
#add button to menu
mainMenu.insert(btn_tt_opc1)
mainMenu.insert(btn_tt_opc2)
mainMenu.insert(btn_tt_opc3)
mainMenu.insert(btn_tt_opc4)
mainMenu.insert(btn_tt_opc5)



