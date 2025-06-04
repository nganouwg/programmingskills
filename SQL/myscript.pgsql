

CREATE SCHEMA IF NOT EXISTS sec;
SELECT * FROM pg_catalog.pg_namespace ORDER BY nspname;

CREATE TABLE irs.nonprofits (
    ein TEXT PRIMARY KEY,
    name TEXT,
    city TEXT,
    state TEXT,
    zip TEXT,
    country TEXT,
    ruling_date TEXT,
    deductibility TEXT,
    foundation TEXT,
    ntee_code TEXT,
    org_type TEXT,
    asset_cd TEXT,
    income_cd TEXT,
    status_cd TEXT,
    subsection TEXT
);

CREATE TABLE sec.file_tracking (
    id SERIAL PRIMARY KEY,
    cik TEXT,
    source TEXT, -- 'companyfacts' or 'submissions'
    filename TEXT UNIQUE,
    status TEXT DEFAULT 'skip', -- 'skip', 'pending', 'loaded', 'failed'
    error_message TEXT,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE sec.companies (
    cik TEXT PRIMARY KEY,
    f_id int,
    name TEXT,
    ticker TEXT,
    exchange TEXT,
    sic TEXT,
    state_of_incorp TEXT,
    address TEXT,
    FOREIGN KEY (f_id) REFERENCES sec.file_tracking(id)
);

CREATE TABLE sec.filings (
    id SERIAL PRIMARY KEY,
    cik TEXT,
    accession_number TEXT,
    form TEXT,
    filed_date DATE,
    report_date DATE,
    FOREIGN KEY (cik) REFERENCES companies(cik)
);

CREATE TABLE sec.facts (
    id SERIAL PRIMARY KEY,
    cik TEXT,
    fact_name TEXT,
    label TEXT,
    uom TEXT,
    value NUMERIC,
    start_date DATE,
    end_date DATE,
    form TEXT,
    FOREIGN KEY (cik) REFERENCES companies(cik)
);


select * from sec.file_tracking 
where "source" = 'submissions' limit 10;

select substring(cik, 1, 13), cik from sec.file_tracking
where cik not like 'CIK__________'

Update sec.file_tracking set cik = substring(cik, 1, 13)
where cik not like 'CIK__________'

select * from sec.file_tracking where status = 'pending'

select * from sec.file_tracking 
where "id" in  
	(
    select id from sec.file_tracking 
    where status in ('skip') limit 25
 	)

update sec.file_tracking set status = 'pending' 
where "id" in  
	(
    select id from sec.file_tracking 
    where status in ('skip') limit 25
 	)