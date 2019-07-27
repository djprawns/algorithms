-- Drop table

-- DROP TABLE public.g4g

CREATE TABLE public.g4g (
	post_id int8 NOT NULL,
	category varchar NULL,
	url varchar NULL,
	created_at timestamp NULL,
	CONSTRAINT g4g_pk PRIMARY KEY (post_id)
);

-- Drop table

-- DROP TABLE public.g4g_category

CREATE TABLE public.g4g_category (
	id serial NOT NULL,
	post_id int8 NULL,
	category varchar NULL,
	CONSTRAINT g4g_category_pk PRIMARY KEY (id),
	CONSTRAINT g4g_category_un UNIQUE (post_id, category)
);
