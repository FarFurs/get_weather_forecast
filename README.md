# Getting weather forecast from wttr.in
This scripts gets data about a weather in certain place from website wttr.in and displays it in terminal

## Environment

### Requirements

Python3 should be already installed. Then use pip (or pip3, if there is a conflict with Python2) to install dependencies:

```bash
pip install -r requirements.txt
```



## Run

Launch on Linux(Python 3) or Windows:

```bash

$ python main.py

```

You will see:

```
svo

     \   /     Солнечно
      .-.      20 °C          
   ― (   ) ―   ← 5 m/s        
      `-’      10 km          
     /   \     2.7 mm         
                        ┌─────────────┐                        
┌───────────────────────┤ Сб. 12 авг. ├───────────────────────┐
│             День      └──────┬──────┘       Ночь            │
├──────────────────────────────┼──────────────────────────────┤
│    \  /       Переменная обл…│  _`/"".-.     Временами умер…│
│  _ /"".-.     25..26 °C      │   ,\_(   ).   19 °C          │
│    \_(   ).   ← 5-7 m/s      │    /(___(__)  ← 5-8 m/s      │
│    /(___(__)  10 km          │    ‚‘‚‘‚‘‚‘   8 km           │
│               0.0 mm | 0%    │    ‚’‚’‚’‚’   2.7 mm | 67%   │
└──────────────────────────────┴──────────────────────────────┘
                        ┌─────────────┐                        
┌───────────────────────┤ Вс. 13 авг. ├───────────────────────┐
│             День      └──────┬──────┘       Ночь            │
├──────────────────────────────┼──────────────────────────────┤
│               Пасмурно       │  _`/"".-.     Небольшой ливн…│
│      .--.     22..25 °C      │   ,\_(   ).   17 °C          │
│   .-(    ).   ↖ 5-6 m/s      │    /(___(__)  ↑ 3-5 m/s      │
│  (___.__)__)  10 km          │      ‘ ‘ ‘ ‘  10 km          │
│               0.0 mm | 0%    │     ‘ ‘ ‘ ‘   0.5 mm | 86%   │
└──────────────────────────────┴──────────────────────────────┘
                        ┌─────────────┐                        
┌───────────────────────┤ Пн. 14 авг. ├───────────────────────┐
│             День      └──────┬──────┘       Ночь            │
├──────────────────────────────┼──────────────────────────────┤
│  _`/"".-.     Небольшой ливн…│  _`/"".-.     Местами дождь  │
│   ,\_(   ).   21 °C          │   ,\_(   ).   18 °C          │
│    /(___(__)  → 3-4 m/s      │    /(___(__)  → 3-6 m/s      │
│      ‘ ‘ ‘ ‘  10 km          │      ‘ ‘ ‘ ‘  10 km          │
│     ‘ ‘ ‘ ‘   0.2 mm | 64%   │     ‘ ‘ ‘ ‘   0.1 mm | 89%   │
└──────────────────────────────┴──────────────────────────────┘

Все новые фичи публикуются здесь: @igor_chubin

london

    \  /       Переменная облачность
  _ /"".-.     21 °C          
    \_(   ).   ↗ 6 m/s        
    /(___(__)  10 km          
               0.0 mm         
                        ┌─────────────┐                        
┌───────────────────────┤ Сб. 12 авг. ├───────────────────────┐
│             День      └──────┬──────┘       Ночь            │
├──────────────────────────────┼──────────────────────────────┤
│               Пасмурно       │               Облачно        │
│      .--.     22 °C          │      .--.     17 °C          │
│   .-(    ).   ↗ 6-7 m/s      │   .-(    ).   ↗ 4-6 m/s      │
│  (___.__)__)  10 km          │  (___.__)__)  10 km          │
│               0.0 mm | 0%    │               0.0 mm | 0%    │
└──────────────────────────────┴──────────────────────────────┘
                        ┌─────────────┐                        
┌───────────────────────┤ Вс. 13 авг. ├───────────────────────┐
│             День      └──────┬──────┘       Ночь            │
├──────────────────────────────┼──────────────────────────────┤
│  _`/"".-.     Местами дождь  │    \  /       Переменная обл…│
│   ,\_(   ).   21 °C          │  _ /"".-.     18 °C          │
│    /(___(__)  ↗ 6 m/s        │    \_(   ).   ↗ 3-5 m/s      │
│      ‘ ‘ ‘ ‘  10 km          │    /(___(__)  10 km          │
│     ‘ ‘ ‘ ‘   0.1 mm | 79%   │               0.0 mm | 0%    │
└──────────────────────────────┴──────────────────────────────┘
                        ┌─────────────┐                        
┌───────────────────────┤ Пн. 14 авг. ├───────────────────────┐
│             День      └──────┬──────┘       Ночь            │
├──────────────────────────────┼──────────────────────────────┤
│  _`/"".-.     Местами дождь  │    \  /       Переменная обл…│
│   ,\_(   ).   23..25 °C      │  _ /"".-.     20 °C          │
│    /(___(__)  ↑ 3-4 m/s      │    \_(   ).   ↗ 2-3 m/s      │
│      ‘ ‘ ‘ ‘  10 km          │    /(___(__)  10 km          │
│     ‘ ‘ ‘ ‘   0.1 mm | 61%   │               0.0 mm | 0%    │
└──────────────────────────────┴──────────────────────────────┘

Все новые фичи публикуются здесь: @igor_chubin

Cherepovets

  _`/"".-.     Местами дождь
   ,\_(   ).   22 °C          
    /(___(__)  ← 1 m/s        
      ‘ ‘ ‘ ‘  10 km          
     ‘ ‘ ‘ ‘   0.1 mm         
                        ┌─────────────┐                        
┌───────────────────────┤ Сб. 12 авг. ├───────────────────────┐
│             День      └──────┬──────┘       Ночь            │
├──────────────────────────────┼──────────────────────────────┤
│               Облачно        │    \  /       Переменная обл…│
│      .--.     26..27 °C      │  _ /"".-.     20 °C          │
│   .-(    ).   ↖ 5-7 m/s      │    \_(   ).   ← 3-6 m/s      │
│  (___.__)__)  10 km          │    /(___(__)  10 km          │
│               0.0 mm | 0%    │               0.0 mm | 0%    │
└──────────────────────────────┴──────────────────────────────┘
                        ┌─────────────┐                        
┌───────────────────────┤ Вс. 13 авг. ├───────────────────────┐
│             День      └──────┬──────┘       Ночь            │
├──────────────────────────────┼──────────────────────────────┤
│               Облачно        │               Облачно        │
│      .--.     23..25 °C      │      .--.     19 °C          │
│   .-(    ).   ← 3-6 m/s      │   .-(    ).   ← 2-6 m/s      │
│  (___.__)__)  10 km          │  (___.__)__)  10 km          │
│               0.0 mm | 0%    │               0.0 mm | 0%    │
└──────────────────────────────┴──────────────────────────────┘
                        ┌─────────────┐                        
┌───────────────────────┤ Пн. 14 авг. ├───────────────────────┐
│             День      └──────┬──────┘       Ночь            │
├──────────────────────────────┼──────────────────────────────┤
│  _`/"".-.     Местами дождь  │    \  /       Переменная обл…│
│   ,\_(   ).   21 °C          │  _ /"".-.     18 °C          │
│    /(___(__)  ↖ 2 m/s        │    \_(   ).   ↗ 1-2 m/s      │
│      ‘ ‘ ‘ ‘  10 km          │    /(___(__)  10 km          │
│     ‘ ‘ ‘ ‘   0.1 mm | 76%   │               0.0 mm | 0%    │
└──────────────────────────────┴──────────────────────────────┘

Все новые фичи публикуются здесь: @igor_chubin
```

## Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org).