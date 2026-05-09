% Hechos sobre comandos SQL

comando(select, 'Consulta datos de una o más tablas').
comando(insert, 'Inserta nuevos registros').
comando(update, 'Modifica registros existentes').
comando(delete, 'Elimina registros').
comando(create, 'Crea objetos de base de datos').
comando(alter, 'Modifica objetos existentes').
comando(drop, 'Elimina objetos de base de datos').

categoria(select, dql).
categoria(insert, dml).
categoria(update, dml).
categoria(delete, dml).
categoria(create, ddl).
categoria(alter, ddl).
categoria(drop, ddl).

join(inner_join).
join(left_join).
join(right_join).
join(full_join).

funcion_agregada(count).
funcion_agregada(sum).
funcion_agregada(avg).
funcion_agregada(min).
funcion_agregada(max).

% Regla: determina si un comando modifica datos
modifica_datos(X) :-
    categoria(X, dml).

% Regla: determina si un comando define estructura
define_estructura(X) :-
    categoria(X, ddl).
