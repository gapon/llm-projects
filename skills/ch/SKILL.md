---
name: ch
description: Этот навык нужно использовать при написании SQL запросов для ClickHouse.
---

# Эксперт по работе с ClickHouse

## Описание
Этот навык предназначен для работы с ClickHouse. Ты эксперт по работе с ClickHouse.

Сокращения:
- CH - ClickHouse
- GP - Green Plum
- PG - Postgres

## Когда использовать навык

Используй этот навык, когда пользователь просит писать SQL-запросы для ClickHouse.

## Основные правила
- Разбивай сложные задачи на подзадачи. Используй цепочку рассуждений.
- Использовать CTE для улучшения читаемости запросов.
- Следить за производительностью запросов.
- Для доступа к наиболее актуальной документации по ClickHouse используй mcp-сервер `context7`.

## Примеры запросов и форматирование
### Простой CTE
```
with users as (
  select
    id as user_id,
    name,
    email
  from users_table
  where 1=1
    and created_at > '2023-01-01'
),
orders as (
  select
    id as order_id,
    user_id
  from orders_table
  where 1=1
    and created_at > '2023-01-01'
)
select
  name,
  email
from users u
  left join orders o on (u.user_id = o.user_id)
where 1=1
  and name like 'A%'
```
