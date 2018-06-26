URL = 'http://api-hack.photolab.me/template_process.php'

templates_names = {
    'versus': ['C8241960-CAE7-E464-C9FD-8553020A9DBA', 'E754366C-914C-BE94-F9EF-0FE946138B92'],
    'soccer_man': '4283E3C4-BE89-42A4-D9B5-B775A66F146F',
    'stadium': '86316D90-67CA-6D64-E933-7B66E1F5B3E5',
    'nature_1': '66FEB7C9-DAE5-7AA4-7560-08B36FD8B385',
    'nature_2': '387FD218-9BEB-3044-D1D2-4FBF6A6CF4C4',
    'nature_3': '390C51FB-F821-C774-B160-79645CD9A64D',
    'nature_4': '088F2063-DB62-F214-AD0D-067DE1628FE3',
    'nature_5': '0471F2CA-F132-CE74-E11B-CA9A8F45C997',
    'nature_6': '315FAF56-7C67-DB44-050A-4D8D57943E62',
    'final_post': 'CFD582FF-A03B-A854-1525-6EE310D97E9D',
    'face_ball': '14917652-6B9A-2374-99AF-66318CFC2C4F',
    'happy': '133A4236-4369-8C64-3585-1F0EFBB62127',
    'cry': '06C37FFD-D932-D9E4-310F-A85A12F2FAF3'
}

numbers = {
    0: 'http://temp-images.ws.pho.to/7bba75f54062916192c054d2efd6e8652fd4af1c.png',
    1: 'http://temp-images.ws.pho.to/71eeb73c458163abb862001de07d52fb12e85ed2.png',
    2: 'http://temp-images.ws.pho.to/8012b7c3c902bf1d8c7a363c96075c2ce022cb09.png',
    3: 'http://temp-images.ws.pho.to/bb2dc1e057e6003d9bf209a4d6d9810aeecb3d08.png',
    4: 'http://temp-images.ws.pho.to/b4fd0862fdcfb0cbd3a758a137e65fea13a125dc.png',
    5: 'http://temp-images.ws.pho.to/77388c10453a2520b80c43c19eda919ec752da01.png',
    6: 'http://temp-images.ws.pho.to/efe6e68536bb6c1f5ad620f94c5f150e7718f385.png',
    7: 'http://temp-images.ws.pho.to/61ae1b79359639097a1be3aeddfc24a35df0975b.png',
    8: 'http://temp-images.ws.pho.to/43cea1b5cab534d7f863e6050eceebb7e0477374.png',
    9: 'http://temp-images.ws.pho.to/cbc1d9391bfa879ab54b2728e2b531dd2d94299e.png'
}

championats = {'Англия, Премьер лига': '12',
               'Россия, Премьер лига': '13',
               'Украина, Премьер лига': '14',
               'Италия, Серия А': '15',
               'Испания, Примера': '16',
               'Германия, Бундеслига': '17',
               'Франция, Лига 1': '18',
               'Лига Чемпионов': '19',
               'Лига Европы': '20',
               'Чемпионат Европы': '24',
               'Чемпионат Мира': '742'
               }

russian2english = {'Россия': 'Russia',
                   'Саудовская Аравия': 'Saudi Arabia',
                   'Португалия': 'Portugal',
                   'Испания': 'Spain',
                   'Марокко': 'Morocco',
                   'Иран': 'IR Iran',
                   'Египет': 'Egypt',
                   'Уругвай': 'Uruguay',
                   'Хорватия': 'Croatia',
                   'Нигерия': 'Nigeria',
                   'Перу': 'Peru',
                   'Дания': 'Denmark',
                   'Аргентина': 'Argentina',
                   'Исландия': 'Iceland',
                   'Франция': 'France',
                   'Австралия': 'Australia',
                   'Бразилия': 'Brazil',
                   'Швейцария': 'Switzerland',
                   'Германия': 'Germany',
                   'Мексика': 'Mexico',
                   'Коста-Рика': 'Costa Rica',
                   'Сербия': 'Serbia',
                   'Тунис': 'Tunisia',
                   'Англия': 'England',
                   'Бельгия': 'Belgium',
                   'Панама': 'Panama',
                   'Швеция': 'Sweden',
                   'Южная Корея': 'Korea Republic',
                   'Польша': 'Poland',
                   'Сенегал': 'Senegal',
                   'Колумбия': 'Colombia',
                   'Япония': 'Japan'
                   }

english2russian = dict(zip(russian2english.values(), russian2english.keys()))


country_flag = {"Russia": 'http://www.world-globe.ru/files/flags/russia_l.png',
                'Saudi Arabia': 'http://www.world-globe.ru/files/flags/saudi-arabia_l.png',
                'Portugal': 'http://www.world-globe.ru/files/flags/portugal_l.png',
                'Spain': 'http://www.world-globe.ru/files/flags/spain_l.png',
                'Morocco': 'http://www.world-globe.ru/countries/morocco/flag/',
                'IR Iran': 'http://www.world-globe.ru/files/flags/iran_l.png',
                'Egypt': 'http://www.world-globe.ru/files/flags/egypt_l.png',
                'Uruguay': 'http://www.world-globe.ru/files/flags/uruguay_l.png',
                'Croatia': 'http://www.world-globe.ru/files/flags/croatia_l.png',
                'Nigeria': 'http://www.world-globe.ru/files/flags/nigeria_l.png',
                'Peru': 'http://www.world-globe.ru/files/flags/peru_l.png',
                'Denmark': 'http://www.world-globe.ru/files/flags/denmark_l.png',
                'Argentina': 'http://www.world-globe.ru/files/flags/argentina_l.png',
                'Iceland': 'http://www.world-globe.ru/files/flags/iceland_l.png',
                'France': 'http://www.world-globe.ru/files/flags/france_l.png',
                'Australia': 'http://www.world-globe.ru/files/flags/australia_l.png',
                'Brazil': 'http://www.world-globe.ru/files/flags/brazil_l.png',
                'Switzerland': 'http://www.world-globe.ru/files/flags/switzerland_l.png',
                'Germany': 'http://www.world-globe.ru/files/flags/germany_l.png',
                'Mexico': 'http://www.world-globe.ru/files/flags/mexico_l.png',
                'Costa Rica': 'http://www.world-globe.ru/files/flags/costa-rica_l.png',
                'Serbia': 'http://www.world-globe.ru/files/flags/serbia_l.png',
                'Tunisia': 'http://www.world-globe.ru/files/flags/tunisia_l.png',
                'England': 'http://www.clipartbest.com/cliparts/RcG/ErL/RcGErLG4i.jpg',
                'Belgium': 'http://www.world-globe.ru/files/flags/belgium_l.png',
                'Panama': 'http://www.world-globe.ru/files/flags/panama_l.png',
                'Sweden': 'http://www.world-globe.ru/files/flags/sweden_l.png',
                'Korea Republic': 'http://www.world-globe.ru/files/flags/south-korea_l.png',
                'Poland': 'http://www.world-globe.ru/files/flags/poland_l.png',
                'Senegal': 'http://www.world-globe.ru/files/flags/senegal_l.png',
                'Colombia': 'http://www.world-globe.ru/files/flags/colombia_l.png'
                }

city2stadium = {'Москва': 'http://otkritiearena.ru/img/event/big/_566.jpg?s=628656',
                'Санкт-Петербург': 'http://liport.ru/uploads/posts/2018-01/igor-albin-stadion-sankt-peterburg-budet-peredan-vkoncessiyu-zenitu_1.jpg',
                'Калининград': 'https://worldcap2018.ru/wp-content/uploads/2017/02/Vid-na-pole-1.jpg',
                'Волгоград': 'https://pbs.twimg.com/media/DUOcZTsXcAAzNM5.jpg',
                'Екатеринбург': 'https://media.nakanune.ru/images/pictures/image_big_127972.jpg',
                'Казань': 'http://stadiums.at.ua/_nw/306/14515256.jpg',
                'Нижний Новгород': 'https://eventticketmaster.com/image/stadiums/stadion-nizhny-novgorod.jpg',
                'Ростов-на-Дону': 'http://rostov-arena.ml/wp-content/uploads/2017/10/rostov-arena-vid-nochyu.jpg',
                'Самара': 'http://progorodsamara.ru/userfiles/picoriginal/img-20160315175656-159.jpg',
                'Саранск': 'https://rg.ru/i/gallery/98c3b2fa/1_506cea07.jpg',
                'Сочи': 'https://tropki.ru/sites/default/files/styles/article/public/previews/17127/stadion-fisht_0.jpg'
           }