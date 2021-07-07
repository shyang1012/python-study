from DbTest.util.DbConnection import DbConnection


def select(conn, sql):
    cur = conn.cursor()
    cur.execute(sql)

    rows = cur.fetchall()
    result = []
    for row in rows:
        data = {
            "AlbumId": row[0]
            , "Title": row[1]
            , "ArtistId": row[2]
            , "ArtistName": row[3]
        }
        result.append(data)
    return result


def get_album_info():
    dbname = "chinook.db"
    conn = DbConnection().create_connection(dbname)
    sql = """
        SELECT AlbumId
        , Title
        , a.ArtistId
        , b.name as ArtistName
        FROM ALBUMS a join artists b on a.ArtistId = b.ArtistId
    """
    albums = select(conn, sql)
    print("AlbumId".ljust(5), "|", "Title".ljust(95), "|", "ArtistId".ljust(2), "|", "ArtistName")
    for data in albums:
        print(str(data.get("AlbumId")).ljust(7), "|", data.get("Title").ljust(95), "|".ljust(5), str(data.get("ArtistId")).ljust(4), "|", data.get("ArtistName"))


if __name__ == '__main__':
    get_album_info()
