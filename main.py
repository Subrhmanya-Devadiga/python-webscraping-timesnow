from bs4 import BeautifulSoup
import sqlite3
import requests
import sys

def headline_print():
    print("\n")
    print("\t\t\t <<<< HEADLINES >>>>")
def line():
    print("___//___" * 20)
    print("\n")

def take_input():
    print("\n")
    print(" >>>  Please select one of the catogery")
    print(" >>> 'HEADLINES'  'GENERAL'  'COVID' 'EXCLUSIVE' 'EXIT' <<< ")

def main():
    html_file = requests.get('https://www.timesnownews.com/').text
    soup = BeautifulSoup(html_file, 'lxml')
    timesnow = soup.find('div',class_='content-block')
    s1 = soup.find('div', class_='section-one')
    take_input()
    choice = input(" >>> ").upper()
    print("\n")

    #headline
    if choice == 'HEADLINES':
        s1_h_text = s1.find('h2',class_='content').text
        link = s1.a['href']
        print("\n")
        print("\t\t <<< TODAY's HEADLINES >>>")
        print("\n")
        print(f"\t {s1_h_text}")
        print(f"\t https://www.timesnownews.com{str(link)}")
        print("\n")

        #section1
        s1_hs = s1.find_all('div',class_='component_1')
        for s1_h in s1_hs:
            s1_h_text = s1_h.find('h3',class_='text').text
            s1_l = s1_h.a['href']
            print(f"\t {s1_h_text.strip()}")
            print(f"\t https://www.timesnownews.com{s1_l.strip()}")
            print("\n")
        #section2
        s2 = timesnow.find('div', class_='section-two')
        s2_hs = s2.find_all('div', class_='component_1')
        for s2_h in s2_hs:
            s2_h_text = s2_h.find('a').get_text()
            s2_h_link = s2_h.a['href']
            print(f"\t {s2_h_text.strip()}")
            print(f"\t https://www.timesnownews.com{s2_h_link.strip()}")
            print("\n")
        line()

    if choice == 'GENERAL':
        #section6 india news
        s6 = timesnow.find('div', class_='section-six')
        s6_s1 = s6.find('div', class_='section-one')
        s6_c4 = s6_s1.find('div',class_='component_4')
        print("\t\t <<<< ALL INDIA NEWS >>>>")
        print("\n")
        s6_c4_text = s6_c4.find('a').get_text()
        s6_c4_link = s6_c4.a['href']
        print(f"\t {s6_c4_text.strip()}")
        print(f"\t https://www.timesnownews.com{s6_c4_link.strip()}")
        print("\n")

        count = 0
        s6_s1 = s6.find_all('div', class_='section-one')
        for s1 in s6_s1:
            s6_c1 = s1.find_all('div',class_='component_1')
            more = s1.find('div',class_='new_more').a['href']
            for c1 in s6_c1:
                count += 1
                if count == 5:
                    print("\t\t\t <<<< SPORTS >>>>")
                    print("\n")
                if count == 9:
                    print("\t\t\t <<< POLITICS >>>")
                    print("\n")
                s6_c1_text = c1.find('a').get_text()
                s6_c1_link = c1.a['href']
                print(f"\t {s6_c1_text.strip()}")
                print(f"\t https://www.timesnownews.com{s6_c1_link.strip()}")
                print('\n')
            print(f"\t >>> For more News visit https://www.timesnownews.com{more.strip()}")
            print("\n")
            line()

    if choice == 'COVID':
        print("\t\t\t <<< COVID NEWS >>>")
        print("\n")
        s9 = timesnow.find('div', class_='section-nine')
        first_grid = s9.find_all('div',class_='first-grid')
        for f_g_content in first_grid:
            f_g_text = f_g_content.h3.find('a').get_text()
            f_g_link = f_g_content.h3.a['href']
            print(f"\t {f_g_text.strip()}")
            print(f"\t https://www.timesnownews.com{f_g_link.strip()}")
            print("\n")
        second_grid = s9.find('div',class_='second-grid')
        s_g_c1 = second_grid.find_all('div',class_='component_1')
        more = s9.find('div',class_='heading')
        more_link = more.a['href']
        for s_g_c1_content in s_g_c1:
            s_g_c1_text = s_g_c1_content.find('a').get_text()
            s_g_c1_link = s_g_c1_content.a['href']
            print(f"\t {s_g_c1_text.strip()}")
            print(f"\t https://www.timesnownews.com{s_g_c1_link.strip()}")
            print("\n")
        print(f"\t >>> For more News visit https://www.timesnownews.com{more_link.strip()}")
        print("\n")
        line()

    if choice == 'EXCLUSIVE':
        print("\t\t\t <<< EXCLUSIVE NEWS >>>")
        print("\n")
        column = timesnow.find('div',class_='column')
        column_2 = column.find('div', class_='column-two') 
        grid_one = column_2.find_all('div',class_='grid-one')
        more = column_2.find('div',class_='component_5')
        more_link = more.a['href']      
        for grid_1 in grid_one:
            component_1 = grid_1.find_all('div',class_='component_1')
            for c_1 in component_1:
                c_1_content = c_1.find('div',class_='content')
                c_1_text = c_1_content.find('a').get_text()
                c_1_link = c_1_content.a['href']
                print(f"\t {c_1_text.strip()}")
                print(f"\t https://www.timesnownews.com{c_1_link.strip()}")
                print("\n")
        print(f"\t >>> For more News visit https://www.timesnownews.com{more_link.strip()}")
        print("\n")
        line()

    if choice == 'EXIT':
        print("\t\t\t >>><<<>>> THANK YOU FOR USING... <<<>>><<<")
        print("\n")
        sys.exit()

def greeting():
    print("\n")
    print("\t\t\t <<<!! WELCOME TO TIMESNOW NEWS !!>>>")
    print("\n")
    print("___//___//"*3 +"  -by subrhmanya devadiga  "+ "___//___//"*3)

greeting()
while True:
    main()
