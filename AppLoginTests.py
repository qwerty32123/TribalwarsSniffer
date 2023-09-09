import time
import unittest
from unittest import TestCase

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
# use this class when we need to wait driver for multiple elements, we create a array with conditions then pass it to
# wedriverwait
class composed_expected_conditions:
    def __init__(self, expected_conditions):
        self.expected_conditions = expected_conditions

    def __call__(self, driver):
        for expected_condition in self.expected_conditions:
            if not expected_condition(driver):
                return False


            return True



# ELEMENTS WE NEED TO IDENTIFY BY ID  FOR LOGIN TESTS
login_elements = {'btn_guest_play': 'air.com.innogames.staemme:id/btn_guest_play',
                  'account_play': 'air.com.innogames.staemme:id/btn_account_play',
                  'server_selection': 'air.com.innogames.staemme:id/layout_welcome',
                  'register': 'air.com.innogames.staemme:id/btn_welcome_registration',
                  'login': 'air.com.innogames.staemme:id/btn_welcome_login',
                  'username_input': 'air.com.innogames.staemme:id/edt_user_name',
                  'password_input': 'air.com.innogames.staemme:id/edt_password',
                  'login_btn': 'air.com.innogames.staemme:id/tv_welcome_action_three',
                  'select_version_bar':'air.com.innogames.staemme:id/tv_welcome_action_two',
                   'cancel_bar':'air.com.innogames.staemme:id/tv_welcome_action_one',
                  'select_world_bar': 'air.com.innogames.staemme:id/ll_welcome_top_bar',
                  'rmnded_world_text': 'air.com.innogames.staemme:id/tv_item_sub_info',
                  'forgot_passwd': 'air.com.innogames.staemme:id/tv_login_forgot_password',
                  'back_arrow_btn':'air.com.innogames.staemme:id/iv_back_action',
                  'map_navigation':'air.com.innogames.staemme:id/map_nav'


                  }

#5 BASIC ELEMENTS FOR NAVIGATE IN THE APP IU
navigation_elements = {
    'account':'air.com.innogames.staemme:id/account_nav',
    'quest':'air.com.innogames.staemme:id/quests_nav',
    'reports':'air.com.innogames.staemme:id/reports_nav',
    'msg':'air.com.innogames.staemme:id/mail_nav',
    'map':'air.com.innogames.staemme:id/map_nav',
    'game':'air.com.innogames.staemme:id/game_nav',
    'menu':'air.com.innogames.staemme:id/menu_nav'
}

ingame_elements = {
    'current_village_field':'air.com.innogames.staemme:id/tv_current_village',
    'menu_label':'air.com.innogames.staemme:id/tvMenuLabel',
    'map_left_btn':'air.com.innogames.staemme:id/btn_map_left',
    'msg_edit_lbl':'air.com.innogames.staemme:id/tvWriteMailLabel',
    'report_category_btn':'air.com.innogames.staemme:id/btn_category',
    'quest_name_lbl':'air.com.innogames.staemme:id/tv_name',
    'btn_exit':'air.com.innogames.staemme:id/btn_exit',
    'rcl_headquarters':'air.com.innogames.staemme:id/rclHeadquarters'


}
menu_elements = {
    'menu_buttons_container':'air.com.innogames.staemme:id/rcvMenu'
}
rally_point_elements = {
    'spear_count':'air.com.innogames.staemme:id/units_entry_all_spear',
    'sword_count':'air.com.innogames.staemme:id/units_entry_all_sword',
    'target_x':'air.com.innogames.staemme:id/inputx',
    'target_y':'air.com.innogames.staemme:id/inputy',
    'form':'air.com.innogames.staemme:id/command-data-form',
    'sword_input':'air.com.innogames.staemme:id/unit_input_sword',
    'spear_input':'air.com.innogames.staemme:id/unit_input_spear',
    'arrival_time':'air.com.innogames.staemme:id/date_arrival',
    'all_units_btn':'air.com.innogames.staemme:id/selectAllUnits'


}






class LoginTests(unittest.TestCase):
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '8'
    desired_caps['automationName'] = 'uiautomator2'
    desired_caps['appActivity'] = 'air.com.innogames.staemme.game.GameActivity'
    desired_caps['appPackage'] = 'air.com.innogames.staemme'
    desired_caps['app'] = '/home/gatopicsa/PycharmProjects/QueensGambitTw/apk/Tribal Wars_3.08.0_Apkpure.apk'


    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)


    user = 'user1'
    password = '123456789'
    server_name = 'International'
    world_name = 'World 133'
    target_x = 567
    target_y = 359
    menu_buttons = {}
    time.sleep(5)
    def app_on_game_init(self):
        try:
            WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.ID, navigation_elements['map'])))

            conditions = [
                EC.presence_of_element_located((By.ID, navigation_elements['map'])),
                EC.presence_of_element_located((By.ID, navigation_elements['account'])),
                EC.presence_of_element_located((By.ID, navigation_elements['game'])),
                EC.presence_of_element_located((By.ID, navigation_elements['menu'])),
                EC.presence_of_element_located((By.ID, navigation_elements['quest'])),

            ]

            WebDriverWait(self.driver, 30).until(composed_expected_conditions(conditions))
            map_nav_btn = self.driver.find_element(By.ID, navigation_elements['map'])
            acc_nav_btn = self.driver.find_element(By.ID, navigation_elements['account'])
            game_nav_btn = self.driver.find_element(By.ID, navigation_elements['game'])
            menu_nav_btn = self.driver.find_element(By.ID, navigation_elements['menu'])
            quest_nav_btn = self.driver.find_element(By.ID, navigation_elements['quest'])
            self.assertTrue(map_nav_btn.is_displayed())
            self.assertTrue(acc_nav_btn.is_displayed())
            self.assertTrue(game_nav_btn.is_displayed())
            self.assertTrue(menu_nav_btn.is_displayed())
            self.assertTrue(quest_nav_btn.is_displayed())
            return True
        except Exception:
            return False

    #We choose to play as an account instead of guest
    def test_01_find_Account_btn(self):
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.ID, login_elements['account_play'])))

        account_play_btn = self.driver.find_element(By.ID,login_elements['account_play'])
        self.assertTrue(account_play_btn.is_displayed())


    #Find account paly btn then click on it.
    def test_02_click_Account_btn(self):
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.ID, login_elements['account_play'])))
        account_play_btn = self.driver.find_element(By.ID,login_elements['account_play'])
        account_play_btn.click()

    #check if  server selection button is visible
    def test_03_search_server_btn(self):
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.ID, login_elements['server_selection'])))
        server_selection = self.driver.find_element(By.ID,login_elements['server_selection'])
        self.assertTrue(server_selection.is_displayed())

    #we click on the server selection button
    def test_04_click_serverchoose_btn(self):
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.ID, login_elements['server_selection'])))
        server_selection = self.driver.find_element(By.ID,login_elements['server_selection'])
        server_selection.click()
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.ID, login_elements['cancel_bar'])))
        cancel_bar = self.driver.find_element(By.ID,login_elements['cancel_bar'])
        self.assertTrue(cancel_bar.is_displayed())

    #we click our server we wanna login for test
    def test_05_click_server(self):
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.ID, login_elements['select_version_bar'])))
        servers = self.driver.find_elements(By.CLASS_NAME,'android.widget.TextView')
        for p in servers:
            if p.text == self.server_name:
                p.click()
                break

        WebDriverWait(self.driver, 10).until_not(EC.presence_of_element_located((By.ID, login_elements['select_version_bar'])))
        with self.assertRaises(NoSuchElementException):
            self.driver.find_element(By.ID,login_elements['select_version_bar'])

    #once we choose our server we click login with account button
    def test_06_click_login_choose_btn(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, login_elements['server_selection'])))

        login_btn = self.driver.find_element(By.ID,login_elements['login'])
        login_btn.click()

        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.ID, login_elements['password_input'])))
        pswd_input = self.driver.find_element(By.ID,login_elements['password_input'])
        self.assertTrue(pswd_input.is_displayed())

    #we input our username and we see if input element equals our username
    def test_07_input_user(self):
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.ID, login_elements['password_input'])))
        user_input = self.driver.find_element(By.ID,login_elements['username_input'])
        user_input.clear()
        user_input.send_keys(self.user)
        self.assertTrue(user_input.text == self.user)
    #we input our password and we see if input element equals our passwrd

    def test_08_input_password(self):
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.ID, login_elements['forgot_passwd'])))
        passw_input = self.driver.find_element(By.ID,login_elements['password_input'])
        passw_input.clear()
        passw_input.send_keys(self.password)
        self.assertTrue(passw_input.text != 'Enter password...')

    #we click login button
    def test_09_perform_login(self):
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.ID, login_elements['username_input'])))
        login = self.driver.find_element(By.ID,login_elements['login_btn'])
        login.click()
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.ID, login_elements['back_arrow_btn'])))
        with self.assertRaises(NoSuchElementException):
            self.driver.find_element(By.ID,login_elements['username_input'])
        arrow_button = self.driver.find_element(By.ID,login_elements['back_arrow_btn'])
        self.assertTrue(arrow_button.is_displayed())

    #we click our world so we join
    def test_10_enter_world(self):
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.ID, login_elements['back_arrow_btn'])))
        servers = self.driver.find_elements(By.CLASS_NAME,'android.widget.TextView')
        for z in servers:
            if z.text == self.world_name:
                z.click()
                break
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.ID, login_elements['map_navigation'])))
        map_acces_button = self.driver.find_element(By.ID,login_elements['map_navigation'])

        self.assertTrue(map_acces_button.is_displayed())

    def test_11_find_all_nav_btns(self):
        self.assertTrue(self.app_on_game_init())
    def test_12_menu_btn(self):
        self.assertTrue(self.app_on_game_init())
        menu_btn = self.driver.find_element(By.ID,navigation_elements['menu'])
        menu_btn.click()
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.ID, ingame_elements['menu_label'])))
        menu_label =  self.driver.find_element(By.ID,ingame_elements['menu_label'])
        self.assertTrue(menu_label.is_displayed())
        self.assertTrue(menu_btn.is_selected())

    def test_13_game_nav_btn(self):
        self.assertTrue(self.app_on_game_init())
        game_btn = self.driver.find_element(By.ID,navigation_elements['game'])
        game_btn.click()
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.ID, ingame_elements['current_village_field'])))
        current_village_lbl = self.driver.find_element(By.ID,ingame_elements['current_village_field'])
        self.assertTrue(current_village_lbl.is_displayed())
        self.assertTrue(game_btn.is_selected())

    def test_14_map_nav_btn(self):
        self.assertTrue(self.app_on_game_init())
        map_btn = self.driver.find_element(By.ID,navigation_elements['map'])
        map_btn.click()
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.ID, ingame_elements['map_left_btn'])))
        map_left_btn = self.driver.find_element(By.ID,ingame_elements['map_left_btn'])
        self.assertTrue(map_btn.is_selected())
        self.assertTrue(map_left_btn.is_displayed())


    def test_15_quests_nav_btn(self):
        self.assertTrue(self.app_on_game_init())
        quests_nav_btn = self.driver.find_element(By.ID,navigation_elements['quest'])
        quests_nav_btn.click()
        self.assertTrue(quests_nav_btn.is_selected())

    def test_16_account_nav_btn(self):
        self.assertTrue(self.app_on_game_init())
        account_nav_btn = self.driver.find_element(By.ID,navigation_elements['account'])
        account_nav_btn.click()
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.ID, ingame_elements['btn_exit'])))
        logout_btn = self.driver.find_element(By.ID,ingame_elements['btn_exit'])
        self.assertTrue(logout_btn.is_displayed())
    def test_17_check_menu_elements(self):
        self.assertTrue(self.app_on_game_init())
        menu_btn = self.driver.find_element(By.ID,navigation_elements['menu'])
        menu_btn.click()
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.ID, menu_elements['menu_buttons_container'])))
        menu = self.driver.find_element(By.ID,menu_elements['menu_buttons_container'])
        all_menu_bubttons = menu.find_elements(By.CLASS_NAME,'android.view.ViewGroup')
        self.load_menu_ids(all_menu_bubttons)

    def test_18_check_headquarters(self):
        self.assertTrue(self.app_on_game_init())
        menu_btn = self.driver.find_element(By.ID,navigation_elements['menu'])
        menu_btn.click()


        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.ID, menu_elements['menu_buttons_container'])))
        menu = self.driver.find_element(By.ID,menu_elements['menu_buttons_container'])
        all_menu_bubttons = menu.find_elements(By.CLASS_NAME,'android.view.ViewGroup')
        for p in all_menu_bubttons:
            name = p.find_element(By.CLASS_NAME,"android.widget.TextView")
            if name.text == 'Headquarters':
                p.click()
                break


        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.ID, ingame_elements['rcl_headquarters'])))
        headquarter_inside_element = self.driver.find_element(By.ID,ingame_elements['rcl_headquarters'])
        self.assertTrue(headquarter_inside_element.is_displayed())
    def test_19_try_to_build(self):
        self.app_on_game_init()
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.ID, ingame_elements['rcl_headquarters'])))
        all_view_groups = self.driver.find_elements(By.CLASS_NAME,'android.view.ViewGroup')
        count = 0
        for p in all_view_groups:
            name = p.find_elements(By.CLASS_NAME,"android.widget.TextView")
            for z in name:
                if 'Upgrade to level' in z.text or 'Construct' in z.text:
                    z.click()
                    count += 1
                    return self.assertTrue(True)
        if count == 0:
            self.assertTrue(False)

    def test_20_attack_barbarian(self):
        self.assertTrue(self.app_on_game_init())

        #Navigate through menu till rally point
        menu_btn = self.driver.find_element(By.ID,navigation_elements['menu'])
        menu_btn.click()

        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.ID, menu_elements['menu_buttons_container'])))
        menu = self.driver.find_element(By.ID,menu_elements['menu_buttons_container'])
        all_menu_bubttons = menu.find_elements(By.CLASS_NAME,'android.view.ViewGroup')
        for p in all_menu_bubttons:
            name = p.find_element(By.CLASS_NAME,"android.widget.TextView")
            if name.text == 'Rally point':
                p.click()
                break

        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.ID,rally_point_elements['all_units_btn'] )))
        #We input target village


        inputx = self.driver.find_element(By.ID,rally_point_elements['target_x'])
        inputy = self.driver.find_element(By.ID,rally_point_elements['target_y'])
        inputy.clear()
        inputx.clear()
        inputx.send_keys(self.target_x)
        inputy.send_keys(self.target_y)
        #we input amount of units
        inputsword = self.driver.find_element(By.ID,rally_point_elements['sword_input'])
        inputspear = self.driver.find_element(By.ID,rally_point_elements['spear_input'])
        inputspear.clear()
        inputsword.clear()
        inputsword.send_keys(2)
        inputspear.send_keys(2)


        entire_form =  self.driver.find_element(By.ID,rally_point_elements['form'])
        rally_views = entire_form.find_elements(By.CLASS_NAME,'android.view.ViewGroup')
        for p in rally_views:
            name = p.find_element(By.CLASS_NAME,"android.widget.Button")
            if name.text == 'Attack':
                p.click()
                break
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.ID, rally_point_elements['arrival_time'])))
        arrival_time = self.driver.find_element(By.ID,rally_point_elements['arrival_time'])
        self.assertTrue(arrival_time.is_displayed())


    def test_21_send_attack(self):
        self.assertTrue(self.app_on_game_init())
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.ID, rally_point_elements['arrival_time'])))
        all_buttons = self.driver.find_elements(By.CLASS_NAME,'android.widget.Button')
        for p in all_buttons:
            if p.text == "Send attack":
                p.click()
                break
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.ID, rally_point_elements['form'])))
        all_buttons = self.driver.find_elements(By.CLASS_NAME,'android.view.View')
        for z in all_buttons:
            if z.text == "cancel":
                z.click()
                break
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.ID, rally_point_elements['sword_input'])))

        inputsword = self.driver.find_element(By.ID,rally_point_elements['sword_input'])
        self.assertTrue(inputsword.is_displayed())

































    def load_menu_ids(self,buttons):
        for p in buttons:
            text = p.find_element_by_id('air.com.innogames.staemme:id/tvMenuName')
            self.menu_buttons[text.text] = text.id
        print(len(buttons))
        print(len(self.menu_buttons))
        self.assertTrue(len(buttons) == len(self.menu_buttons))





if __name__ == '__main__':
    unittest.main()




