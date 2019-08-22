
class Contact:
    def __init__(self, name, phone_number, email, addr):
        self.name=name
        self.phone_number=phone_number
        self.email=email
        self.addr=addr
    def print_info(self):
        print("이름:", self.name)
        print("전화번호:", self.phone_number)
        print("이메일:", self.email)
        print("주소;", self.addr)

def print_menu():
    print('1. 연락처 입력')
    print('2. 연락처 출력')
    print('3. 연락처 삭제')
    print('4. 종료')
    menu=input('메뉴선택:')
    return int(menu)

def set_contact():
   name = input("이름은?")
   phone_number=input("전화번호는?")
   email=input("이메일은?")
   addr=input("주소는?")

   c = Contact(name,phone_number,email,addr)
   return c

def print_contact(contact_list):
  for n in contact_list:
        n.print_info()

def delete_contact(contact_list, name):
    for n in contact_list:
        if n.name == name:
            contact_list.remove(n)



def run():
    # Contact 인스턴스를 저장할 리스트 자료구조 생성
    contact_list = []
    while True:
        menu=print_menu()
        if menu==4:  # 종료를 선택하면
            break
        elif menu==1: # 입력을 선택하면
            contact = set_contact()
            contact_list.append(contact)
        elif menu==2: # 출력을 선택하면
            print_contact(contact_list)
        elif menu==3: # 삭제를 선택하면
            name = input('삭제할 이름은?')
            delete_contact(contact_list,name)


if __name__ == "__main__":
    run()