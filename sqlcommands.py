def sqlcreate(cur):
	command_create = """
	CREATE TABLE public."hist_results"
	(
		"OutID" text COLLATE pg_catalog."default" NOT NULL,
	    "Birth" integer NOT NULL,
	    "SEXTYPENAME"	text COLLATE pg_catalog."default",
	    "REGNAME"	text COLLATE pg_catalog."default",
	    "AREANAME" text COLLATE pg_catalog."default",
	    "TERNAME"	text COLLATE pg_catalog."default",
	    "REGTYPENAME"	text COLLATE pg_catalog."default",
	    "TerTypeName"	text COLLATE pg_catalog."default",
	    "ClassProfileNAME" text COLLATE pg_catalog."default",	
	    "ClassLangName" text COLLATE pg_catalog."default",
	    "EONAME" text COLLATE pg_catalog."default",
	    "EOTYPENAME" text COLLATE pg_catalog."default",
	    "EORegName" text COLLATE pg_catalog."default",
	    "EOAreaName" text COLLATE pg_catalog."default",
	    "EOTerName" text COLLATE pg_catalog."default",
	    "EOParent" text COLLATE pg_catalog."default",
	    "UkrTest"	text COLLATE pg_catalog."default",
	    "UkrTestStatus" text COLLATE pg_catalog."default",
	    "UkrBall100" real,
	    "UkrBall12" integer,
	    "UkrBall" integer,
	    "UkrAdaptScale" integer,
	    "UkrPTName" text COLLATE pg_catalog."default",
	    "UkrPTRegName" text COLLATE pg_catalog."default",
	    "UkrPTAreaName" text COLLATE pg_catalog."default",
	    "UkrPTTerName" text COLLATE pg_catalog."default",
	    "histTest" text COLLATE pg_catalog."default",	
	    "HistLang" text COLLATE pg_catalog."default",
	    "Status" text COLLATE pg_catalog."default",	
	    "Score" real,
	    "histBall12" integer,
	    "histBall" integer,
	    "histPTName" text COLLATE pg_catalog."default",
	    "Region" text COLLATE pg_catalog."default",
	    "histPTAreaName" text COLLATE pg_catalog."default",
	    "histPTTerName" text COLLATE pg_catalog."default",
	    "mathTest" text COLLATE pg_catalog."default",
	    "mathLang" text COLLATE pg_catalog."default",
	    "mathTestStatus" text COLLATE pg_catalog."default",
	    "mathBall100" real,
	    "mathBall12" integer,
	    "mathBall" integer,
	    "mathPTName" text COLLATE pg_catalog."default",
	    "mathPTRegName" text COLLATE pg_catalog."default",
	    "mathPTAreaName" text COLLATE pg_catalog."default",
	    "mathPTTerName" text COLLATE pg_catalog."default",
	    "physTest" text COLLATE pg_catalog."default",
	    "physLang" text COLLATE pg_catalog."default",
	    "physTestStatus" text COLLATE pg_catalog."default",
	    "physBall100" real,
	    "physBall12" integer,
	    "physBall" integer,
	    "physPTName" text COLLATE pg_catalog."default",
	    "physPTRegName" text COLLATE pg_catalog."default",
	    "physPTAreaName" text COLLATE pg_catalog."default",
	    "physPTTerName" text COLLATE pg_catalog."default",
	    "chemTest" text COLLATE pg_catalog."default",
	    "chemLang" text COLLATE pg_catalog."default",
	    "chemTestStatus" text COLLATE pg_catalog."default",
	    "chemBall100" real,
	    "chemBall12" integer,
	    "chemBall" integer,
	    "chemPTName" text COLLATE pg_catalog."default",
	    "chemPTRegName" text COLLATE pg_catalog."default",
	    "chemPTAreaName" text COLLATE pg_catalog."default",
	    "chemPTTerName" text COLLATE pg_catalog."default",
	    "bioTest" text COLLATE pg_catalog."default",
	    "bioLang" text COLLATE pg_catalog."default",
	    "bioTestStatus" text COLLATE pg_catalog."default",
	    "bioBall100" real,
	    "bioBall12" integer,
	    "bioBall" integer,
	    "bioPTName" text COLLATE pg_catalog."default",
	    "bioPTRegName" text COLLATE pg_catalog."default",
	    "bioPTAreaName" text COLLATE pg_catalog."default",
	    "bioPTTerName" text COLLATE pg_catalog."default",
	    "geoTest" text COLLATE pg_catalog."default",
	    "geoLang" text COLLATE pg_catalog."default",
	    "geoTestStatus" text COLLATE pg_catalog."default",
	    "geoBall100" real,
	    "geoBall12" integer,
	    "geoBall" integer,
	    "geoPTName" text COLLATE pg_catalog."default",
	    "geoPTRegName" text COLLATE pg_catalog."default",
	    "geoPTAreaName" text COLLATE pg_catalog."default",
	    "geoPTTerName" text COLLATE pg_catalog."default",
	    "engTest" text COLLATE pg_catalog."default",
	    "engTestStatus" text COLLATE pg_catalog."default",
	    "engBall100" real,
	    "engBall12" integer,
	    "engDPALevel" text COLLATE pg_catalog."default",
	    "engBall" integer,
	    "engPTName" text COLLATE pg_catalog."default",
	    "engPTRegName" text COLLATE pg_catalog."default",
	    "engPTAreaName" text COLLATE pg_catalog."default",
	    "engPTTerName" text COLLATE pg_catalog."default",
	    "fraTest" text COLLATE pg_catalog."default",
	    "fraTestStatus" text COLLATE pg_catalog."default",
	    "fraBall100" real,
	    "fraBall12" integer,
	    "fraDPALevel" text COLLATE pg_catalog."default",
	    "fraBall" integer,
	    "fraPTName" text COLLATE pg_catalog."default",
	    "fraPTRegName" text COLLATE pg_catalog."default",
	    "fraPTAreaName" text COLLATE pg_catalog."default",
	    "fraPTTerName" text COLLATE pg_catalog."default",
	    "deuTest" text COLLATE pg_catalog."default",
	    "deuTestStatus" text COLLATE pg_catalog."default",
	    "deuBall100" real,
	    "deuBall12" integer,
	    "deuDPALevel" text COLLATE pg_catalog."default",
	    "deuBall" integer,
	    "deuPTName" text COLLATE pg_catalog."default",
	    "deuPTRegName" text COLLATE pg_catalog."default",
	    "deuPTAreaName" text COLLATE pg_catalog."default",
	    "deuPTTerName" text COLLATE pg_catalog."default",
	    "spaTest" text COLLATE pg_catalog."default",
	    "spaTestStatus" text COLLATE pg_catalog."default",
	    "spaBall100" real,
	    "spaBall12" integer,
	    "spaDPALevel" text COLLATE pg_catalog."default",
	    "spaBall" integer,
	    "spaPTName" text COLLATE pg_catalog."default",
	    "spaPTRegName" text COLLATE pg_catalog."default",
	    "spaPTAreaName" text COLLATE pg_catalog."default",
	    "spaPTTerName" text COLLATE pg_catalog."default",
	    "Year" integer NOT NULL,
	    CONSTRAINT "Hist_results_pkey" PRIMARY KEY ("OutID")
	)
	"""
	cur.execute(command_create)
	return cur

def sqldrop(cur):
	command_drop = "DROP TABLE hist_results;"
	cur.execute(command_drop)
	return cur

def sqlselect(cur):
	command_select = '''SELECT "Region", min("Score"), "Year" FROM public.hist_results
	WHERE "Status" = '????????????????????'
	GROUP BY "Region", "Year"
	ORDER BY "Region", "Year";'''
	cur.execute(command_select)
	return cur

def sqlinsert(cur, values):
	command_insert = "INSERT INTO hist_results VALUES(%s)"
	cur.execute(command_insert % (", ".join(values)))
	return cur