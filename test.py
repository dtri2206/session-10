import streamlit as st

st.title('Trà Sữa CoTAI')

a,b=st.columns(2)
with a:
  st.image('https://i.imgur.com/lEpdPsT.jpeg')
with b:
  l=st.radio('Kích cỡ',('Nhỏ (30K)','Vừa (40K)','Lớn (50K)'))
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
  elif l == 'Vừa (40K': l = 'Vừa'
  elif l == 'Lớn (50K)': l = 'Lớn'
  st.success(f'Cỡ: {l}')

  if l == 'Nhỏ': money = 30
  elif l == 'Vừa': money = 40
  else: money = 50

  a = []
  if sua == True: 
    a.append('Sữa') 
    money +=5 
  if caphe == True: 
    a.append('Cà phê')
    money +=8
  if kem == True: 
    a.append('Kem')
    money += 10
  if trung == True: 
    a.append('Trứng')
    money += 15
  nstr = 'Thêm:'
  for i in len(a):
    if i == 0: nstr += a[i]
    nstr = nstr + "," + a[i]
  st.success(nstr)
  st.success('Topping:', *d)
  for i in d:
    if i =='Trân châu trắng (5K)':money += 5
    if i =='Trân châu đen (5K)': money += 5
    if i =='Thạch rau câu (6K)':money += 6
    if i =='Vải (7K)':money += 7
    if i =='Nhãn (8K)':money += 8
    if i =='Đào (10K)':money += 10

  st.success(textarea)

  money = money * soluong
  st.success(f'Số lượng: {soluong}')

  st.success(f'Thành tiền: {money}K')
