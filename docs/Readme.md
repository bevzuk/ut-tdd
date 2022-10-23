## 1.1. TODO:
* [ ] Todo 1

## 1.2. Links
* (GitHub репозиторий)[https://github.com/bevzuk/ut-tdd]
* (Фото тренинга в Самаре)[https://photos.app.goo.gl/vVmrkP3rFsQvY37a7]
* (Фото тренинга в Райфе)[https://disk.yandex.ru/d/150AIWfx3GU3BP]
* (Фото тренинга в Алмате)[https://photos.app.goo.gl/p2AUx62YYN4P2R9x5]

## 1.3. Подготовка

* [Source code](https://github.com/bevzuk/ut-tdd)

Получить последнюю версию
``` text
cd ~/<your working folder>
git clone https://github.com/bevzuk/ut-tdd.git
git checkout -b <your branch>
```

## Структура
1. [Начало](01.Начало.md)
2. [Парное программирование](02.Парное_программирование.md)
3. [Unit Test](03.Unit_Test.md)
4. [Fixture](04.Fixture.md)
5. [Stub/Mock/Spy](05.Дублеры.md)
6. [3 столба тестирования; Паттерны разработки модульных тестов](06.Patterns_and_Antipatterns.md)
7. [Тестирование legacy кода](07.Legacy.md)
8. [Тестирование UI](08.Testing_UI.md)
9. [Domain Specific Language (DSL)](09.DSL.md)
10. [Behaviour Driven Development (BDD)](10.BDD.md)
11. [Test Driven Development (TDD)](11.TDD.md)
12. [Transformation Priority Premise (TPP)](12.Transformation_Priority_Premise.md)
13. [Object Calisthenics](13.Object_Calisthenics.md)
14. [Шаблоны красной и зеленой полосы](14.Шаблоны_красной_и_зеленой_полосы.md)
15. [Принципы разработки](15.Принципы_разработки.md)
16. [Паттерны тестируемого дизайна](16.Паттерны_тестируемого_дизайна.md)
17. [Модель принятия решений](17.Модель_принятия_решений.md)
18. [Завершение](18.Завершение.md)

## 1.5. Unit Testing




## Непонятные блоки
-   Роль фикстуры
    -   Фреймворк модульного тестирования 
    -   Разработка тест-кейса
    -   Разработка теста
    -   Простые сравнения
    -   Сложные сравнения
    -   Таймауты
    -   Исключения
    -   Параметризованные тесты

1.  ### Упражнение. Покрытие тестами легаси кода
    -   Задача: Попробовать ручками несколько приемов рефакторинга
        легаси кода с целью повышения тестируемости
        -   Extract & Override
        -   Рефакторинг статических классов в экземплярные
        -   Избавление от инфраструктурных зависимостей на примере
            DateTime.Now()
              

2.  ### Упражнение. Инъекция зависимостей

    -   Задача: Используя принцип DIP, внедрить зависимости между
        объектами разными способами
        -   Выделение интерфейса
        -   Инъекция через конструктор
        -   Инъекция через свойство или метод
        -   Инъекция через фабрику  
              

3.  ### Упражнение. IoC фреймворки

    -   Задача: Переписать ранее написанный код и тесты, используя IoC
        фреймворк
        -   Инъекция через конструктор с использованием IoC
        -   Инъекция через свойство или метод с использованием IoC  
              

4.  ### Упражнение. Иерархия тестовых классов

    -   Задача. Переписать ранее созданные тесты, вынеся общую логику в
        базовые классы
        -   Абстрактный инфраструктурный класс  
              

## 1.6. Ретроспектива


## 1.8. План на День 2

-   Хороший юнит тест
-   Квадранты тестирования
-   Mock фреймворки
-   Паттерны тестируемого дизайна
-   Тестирование UI
-   Паттерны и антипаттерны модульных тестов
-   Тестирование унаследованного кода
-   DSL как способ написания тестов на языке бизнеса

  
------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------

# 2. TDD

## 3.3. Программа тренинга


Преимущества и недостатки TDD

-   Самостоятельное обсуждение
-   Дебриф

Внедрение в процесс разработки

-   Затраты на TDD
-   Постановка экономической задачи
-   Общение с менеджментом
-   Secure sandbox
-   Последовательное расширение tdd scope

Типовые ошибки использования и внедрения

-   Code First
-   Too Many Obvious Implementation
-   Too Many Triangulations
-   Coverage Affinity
-   Implementation Testing not Contract Testing

Переход от TDD к ATDD

Вопросы и ответы

-   Приемы из реальной жизни.
-   Как и когда писать тесты?
-   Как и когда фиксить баги?
-   Как работать с легаси кодом и как гасить технический долг?
-   Как писать тесты на легаси код?
-   Как выглядит рабочий день девелопера?

Заключение


## 3.5. Упражнения

### 3.5.5. Упражнение 5. Рулетка
-   Я, как казино, могу предложить игрокам сыграть в рулетку
-   Я, как игра, выбрасываю числа от 0 до 36 с равной вероятностью
-   Я, как игрок, могу делать ставки на чет/нечет. Выигрышный
    коэффициент = 1
-   Я, как игрок, теряю половину ставки при выпадении 0

## 3.7. Какие навыки получат участники?

-   Смогут автоматизировать ручную работу.
-   Поймут, какую ценность несет Unit Testing и TDD.
-   Отработают механику TDD на практике.
-   Увидят, как строить дизайн постепенно, маленькими шагами.
-   Смогут двигаться с постоянной скоростью.
-   Поймут, как больше заниматься творческой, а не рутинной работой.
-   Увидят, как больше времени тратить на написание кода, а не
    "затяжной" дебаг.

## 3.8. Ценность для бизнеса

-   Делать тот продукт, который хочет заказчик (а не тот, который описан
    в документации)
-   Вносить изменения в продукт легче и дешевле.
-   Существенно снизить количество новых багов.
-   Раньше получать прибыль от продукта.
-   Увеличить мотивацию разработчиков.

## 3.9. Участники

-   .Net или С++ разработчики
-   Количество: 8 человек

## 3.10. Требования к участникам

-   Ноутбук с зарядкой
-   Visual Studio 2012 или 2013
-   ReSharper или Visual Assist
-   Git

## 3.11. Требования к помещению

-   Проектор
-   Wi-Fi
-   Столы, чтобы людям было комфортно сидеть в парах
-   Флипчарты (3 шт.)
-   Маркеры для флипчартов

ToDo List

-   Прочитать про шаблоны TDD
-   Настроить ветки
-   Настроить TeamCity
-   Маркеры
-   Скотч
-   Зарядка, удлинитель, адаптеры