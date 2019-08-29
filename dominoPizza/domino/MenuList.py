class Menu:
    def __init__(self,menu_name,menu_price,menu_desc,menu_cate,menu_img): #생성자 함수
        self.menu_name = menu_name
        self.menu_price = menu_price
        self.menu_desc = menu_desc
        self.menu_cate = menu_cate
        self.menu_img = menu_img

    def result(self):
        print('{0}정보를 추가 하였습니다.'.format(self.menu_name))


s=Menu("피자",3000,"맛있어요","피자","이미지")

