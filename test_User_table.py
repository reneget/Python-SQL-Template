from DataBase import get_db_config, database_connection_init
def main():
    dbconfig = get_db_config()
    database_connection_init(dbconfig.build_postgresql_url)
    print(dbconfig)
    




if __name__ == '__main__':
    main()