# import ast
# import time
#
# from sqlalchemy import create_engine
# from sqlalchemy.orm import Session
#
#
# def get_stuff():
#     owner_id = str(message.from_user.id)
#     engine = create_engine(
#         f'postgresql://etmlokgwbnykro:c41c54ac5c89c73e23a3ee26e827115b04acbdf6322a5cefad144bab37ae1aef@ec2-52-4-87-74.compute-1.amazonaws.com:5432/d5n6nt2sh4lhdl')
#     session = Session(bind=engine)
#     query = session.execute(
#         f'SELECT * FROM webapp_stuff WHERE profile={owner_id}').fetchall()
#     if query != None:
#         await call.answer(f'Вы успешно вошли как сотрудник своего ресторана', show_alert=True)
#         restaurant_id = query[0][2]
#         restaurant_name = session.execute(
#             f'SELECT * FROM webapp_restaurant WHERE id={restaurant_id}').fetchall()[0][1]
#         last_order = session.execute(
#             f'SELECT * FROM webapp_order WHERE restaurant_id={restaurant_id} ORDER BY date_of_create DESC').first()
#         names_prices = dict(zip(ast.literal_eval(last_order[0][1]), ast.literal_eval(last_order[0][2])))
#         for key in names_prices:
#             bot.send_message(key, '->', names_prices[key])
#         while True:
#             time.sleep(300)
#             if last_order != session.execute(
#                     f'SELECT * FROM webapp_order WHERE restaurant_id={restaurant_id} ORDER BY date_of_create DESC').first():
#                 last_order = session.execute(
#                     f'SELECT * FROM webapp_order WHERE restaurant_id={restaurant_id} ORDER BY date_of_create DESC').first()
#                 names_prices = dict(zip(ast.literal_eval(last_order[0][1]), ast.literal_eval(last_order[0][2])))
#                 for key in names_prices:
#                     bot.send_message(key, '->', names_prices[key])
#         i = 0
#         while i < len(orders)
#             i += 1
#             print(key, '->', names_prices[key])
#
#     else:
#         await call.answer(f'Вы не сотрудник 😡', show_alert=True)
#
#
# get_stuff()
