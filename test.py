import streamlit as st

st.title('Trà Sữa CoTAI')

a,b=st.columns(2)
with a:
  st.image('https://i.imgur.com/lEpdPsT.jpeg')
with b:
  l=st.radio('Kích cỡ',('Nhỏ (30K)','Vừa (40K)','Lớn (50K)'),horizontal = True)
  st.write('Thêm')
  b1,b2=st.columns(2)
  with b1:
    sua = st.checkbox('Sữa (5K)')
    caphe = st.checkbox('Cà phê (8K)')
  with b2:
    kem = st.checkbox('Kem (10K)')
    trung = st.checkbox('Trứng (15K)')

a1,b1 = st.columns(2)
with a1:d = st.multiselect('Topping', ['Trân châu trắng (5K)', 'Trân châu đen (5K)', 'Thạch rau câu (6K)', 'Vải (7K)', 'Nhãn (8K)', 'Đào (10K)'])
with b1:soluong = st.number_input('Số lượng', step = 1)

textarea = st.text_area('Ghi chú')

if st.button('Đặt hàng', use_container_width=True):
  if l == 'Nhỏ (30K)': l = 'Nhỏ'
  if l == 'Vừa (40K)': l = 'Vừa'
  if l == 'Lớn (50K)': l = 'Lớn'

  if l == 'Nhỏ': money = 30
  if l == 'Vừa': money = 40
  else: money = 50

  a0 = []
  if sua == True: 
    a0.append('Sữa') 
    money +=5 
  if caphe == True: 
    a0.append('Cà phê')
    money +=8
  if kem == True: 
    a0.append('Kem')
    money += 10
  if trung == True: 
    a0.append('Trứng')
    money += 15

  nstr = 'Thêm: '
  for z in range(len(a0)):
    if z == 0:nstr += a0[z]
    else:nstr = nstr + ', ' + a0[z]

  chuoi = 'Topping: '
  for i in range(len(d)):
    if i == 0:chuoi += d[i]
    else: chuoi = chuoi + ', ' + d[i]
  for i in d:
    if i =='Trân châu trắng (5K)':money += 5
    if i =='Trân châu đen (5K)': money += 5
    if i =='Thạch rau câu (6K)':money += 6
    if i =='Vải (7K)':money += 7
    if i =='Nhãn (8K)':money += 8
    if i =='Đào (10K)':money += 10
  money = money * soluong

  tong = f'''Cỡ: {l}
\n{nstr}
\n{chuoi}
\n{textarea}
\n Số lượng: {soluong}
\n Thành tiền: {money}K
'''
  st.success(tong)