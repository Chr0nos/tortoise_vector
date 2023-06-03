We assume that the `vector` extenssion will be installed in the `public` schema

```
database-> \dx
                        List of installed extensions
  Name   | Version |   Schema   |                Description
---------+---------+------------+--------------------------------------------
 plpgsql | 1.0     | pg_catalog | PL/pgSQL procedural language
 vector  | 0.4.1   | public     | vector data type and ivfflat access method
(2 rows)

database-> public.array_to_vector
database-> \df
                                              List of functions
 Schema |             Name              |  Result data type  |          Argument data types           | Type
--------+-------------------------------+--------------------+----------------------------------------+------
 public | array_to_vector               | vector             | double precision[], integer, boolean   | func
 public | array_to_vector               | vector             | integer[], integer, boolean            | func
 public | array_to_vector               | vector             | numeric[], integer, boolean            | func
 public | array_to_vector               | vector             | real[], integer, boolean               | func
 public | avg                           | vector             | vector                                 | agg
 public | cosine_distance               | double precision   | vector, vector                         | func
 public | inner_product                 | double precision   | vector, vector                         | func
 public | ivfflathandler                | index_am_handler   | internal                               | func
 public | l2_distance                   | double precision   | vector, vector                         | func
 public | vector                        | vector             | vector, integer, boolean               | func
 public | vector_accum                  | double precision[] | double precision[], vector             | func
 public | vector_add                    | vector             | vector, vector                         | func
 public | vector_avg                    | vector             | double precision[]                     | func
 public | vector_cmp                    | integer            | vector, vector                         | func
 public | vector_combine                | double precision[] | double precision[], double precision[] | func
 public | vector_dims                   | integer            | vector                                 | func
 public | vector_eq                     | boolean            | vector, vector                         | func
 public | vector_ge                     | boolean            | vector, vector                         | func
 public | vector_gt                     | boolean            | vector, vector                         | func
 public | vector_in                     | vector             | cstring, oid, integer                  | func
 public | vector_l2_squared_distance    | double precision   | vector, vector                         | func
 public | vector_le                     | boolean            | vector, vector                         | func
 public | vector_lt                     | boolean            | vector, vector                         | func
 public | vector_ne                     | boolean            | vector, vector                         | func
 public | vector_negative_inner_product | double precision   | vector, vector                         | func
 public | vector_norm                   | double precision   | vector                                 | func
 public | vector_out                    | cstring            | vector                                 | func
 public | vector_recv                   | vector             | internal, oid, integer                 | func
 public | vector_send                   | bytea              | vector                                 | func
 public | vector_spherical_distance     | double precision   | vector, vector                         | func
 public | vector_sub                    | vector             | vector, vector                         | func
 public | vector_to_float4              | real[]             | vector, integer, boolean               | func
 public | vector_typmod_in              | integer            | cstring[]                              | func
(33 rows)
```
