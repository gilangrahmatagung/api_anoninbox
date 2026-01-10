CREATE TABLE IF NOT EXISTS public.users (
	user_uid bigserial PRIMARY KEY,
	username varchar NOT NULL UNIQUE,
	-- tambah full_name nanti
	is_verified boolean NOT NULL DEFAULT FALSE,
	email varchar NOT NULL UNIQUE,
	password_hash varchar NOT NULL,

	created_at timestamptz NOT NULL DEFAULT NOW(),
	updated_at timestamptz NULL
);