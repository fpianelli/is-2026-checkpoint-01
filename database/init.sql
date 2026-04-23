drop table if exists members;

create table
    members (
        id serial primary key,
        legajo int not null,
        nombre text not null,
        apellido text not null,
        feature text,
        servicio text,
        estado text
    );

insert into
    members (
        legajo,
        nombre,
        apellido,
        feature,
        servicio,
        estado
    )
values
    (
        31477,
        'Felipe',
        'Pianelli',
        'feature01',
        'coordination',
        'activo'
    ),
    (
        31481,
        'Santiago',
        'Sereno',
        'feature02',
        'frontend',
        'activo'
    ),
    (
        31147,
        'Federico',
        'Alvarez Pieroni',
        'feature03',
        'backend',
        'activo'
    ),
    (
        33374,
        'Tiago',
        'Solis',
        'feature04',
        'database',
        'activo'
    ),
    (
        32874,
        'Facundo',
        'Gomez',
        'feature05',
        'portainer',
        'activo'
    );

select
    *
from
    members;