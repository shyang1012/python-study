from Chapter6.config import create_connection, DATA_BASE


class BbsService:
    def __init__(self):
        self.totalCount = 0
        self.listSize = 10
        self.pageSize = 10
        self.totalPage = 0
        self.pageNo = 0
        self.searchParam = ""
        self.firstPageNo = 1
        self.prevPageNo = 0
        self.startPageNo = 1  # 시작 페이지(페이징 기준)
        self.endPageNo = 0  # 끝 페이지(페이징 기준)
        self.nextPageNo = 0
        self.finalPageNo = 0  # 마지막 페이지번호

    def getBBSList(self, searchParam, pageNo) -> object:
        self.pageNo = pageNo
        self.searchParam = searchParam

        sql = f"""
            select bid ,
                    writer ,
                    subject ,
                    content,
                    regDate, 
                    ifnull(readCount,0)  readCount
                from BBS a
        """
        if searchParam != "":
            sql = sql + f"""WHERE content like '%{searchParam}%' or subject like '%{searchParam}%'
            """
        sql = sql + "ORDER BY BID DESC\n"
        sql = sql + f"""LIMIT {self.listSize} OFFSET {(pageNo - 1) * self.listSize}"""

        conn = create_connection(DATA_BASE)
        print("Data base", DATA_BASE)
        print(sql)
        result = []
        with conn:
            cur = conn.cursor()
            cur.execute(sql)

            rows = cur.fetchall()
            for row in rows:
                data = {
                    "bid": row[0]
                    , "writer": row[1]
                    , "subject": row[2]
                    , "content": row[3]
                    , "regDate": row[4]
                    , "readCount": row[5]
                }
                result.append(data)

        return result

    def getBBSTotalCount(self, searchParam) -> object:
        sql = f"""
               select count(*)
                   from BBS a
           """
        if searchParam != "":
            sql = sql + f"""WHERE content like '%{searchParam}%'"""
        conn = create_connection(DATA_BASE)
        print("Data base", DATA_BASE)
        print(sql)
        result = 0
        with conn:
            cur = conn.cursor()
            cur.execute(sql)

            rows = cur.fetchall()
            for row in rows:
                result = row

        return result[0]

    def getBBS(self, bid):

        sql = f"""
            select bid ,
                    writer ,
                    subject ,
                    content,
                    regDate  
                    ,ifnull(readCount,0) readCount
                from BBS a
                WHERE bid = '{bid}' 
        """

        conn = create_connection(DATA_BASE)
        print("Data base", DATA_BASE)
        print(sql)
        result = {}
        with conn:
            cur = conn.cursor()
            cur.execute(sql)

            rows = cur.fetchall()
            for row in rows:
                result = {
                    "bid": row[0]
                    , "writer": row[1]
                    , "subject": row[2]
                    , "content": row[3]
                    , "regDate": row[4]
                    , "readCount": row[5]
                }

        return result

    def saveBBS(self, data):
        sql = ''' INSERT INTO BBS(  bid ,
                                    writer ,
                                    subject ,
                                    content 
                                )
                     VALUES((SELECT max(ifnull(bid,1))+1 from BBS),?,?,?) '''
        conn = create_connection(DATA_BASE)
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()
        return cur.lastrowid

    def updateBBSContent(self, data):
        sql = ''' UPDATE BBS SET
               writer = ?,
                subject = ?,
                content = ?
                WHERE bid = ?
         '''
        conn = create_connection(DATA_BASE)
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()
        return cur.lastrowid

    def updateCount(self, data):
        sql = ''' UPDATE BBS SET
                  readCount = ?
                WHERE bid = ?
            '''
        conn = create_connection(DATA_BASE)
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()
        return cur.lastrowid

    def deleteBbsContens(self, data):
        sql = ''' DELETE FROM BBS
                   WHERE bid = ?
            '''
        conn = create_connection(DATA_BASE)
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()
        return cur.lastrowid

    def getPagingInfo(self):
        self.totalCount = self.getBBSTotalCount(self.searchParam)

        if self.pageNo == 0:
            self.pageNo = 1

        self.totalPage = int(self.totalCount / self.pageSize) + 1

        finalPage = self.totalPage  # 마지막 페이지

        if self.pageNo > finalPage:
            self.pageNo = finalPage

        if self.pageNo < 0 or self.pageNo > finalPage:
            self.pageNo = 1

        isNowFirst = self.pageNo == 1
        isNowFinal = self.pageNo == finalPage

        blockNum = int((self.pageNo - 1) / self.pageSize)
        print("blockNum=", blockNum)
        self.startPageNo = int(self.pageSize * blockNum) + 1
        print("self.startPageNo", self.startPageNo)
        self.endPageNo = self.startPageNo + 10 - 1

        if self.endPageNo > finalPage:
            self.endPageNo = finalPage

        self.firstPageNo = 1

        if isNowFirst:
            self.prevPageNo = 1
        else:
            if (self.pageNo - 1) < 1:
                self.prevPageNo = 1
            else:
                self.prevPageNo = self.pageNo - 1

        if isNowFinal:
            self.nextPageNo = finalPage
        else:
            if (self.pageNo + 1) > finalPage:
                self.nextPageNo = finalPage
            else:
                self.nextPageNo = self.pageNo + 1

        self.finalPageNo = finalPage

        num = self.totalCount - (self.pageNo - 1) * self.listSize
        print("num", num)
        result = {
            "totalCount": self.totalCount
            , "totalPage": self.totalPage
            , "startPageNo": self.startPageNo
            , "endPageNo": self.endPageNo
            , "prevPageNo": self.prevPageNo
            , "nextPageNo": self.nextPageNo
            , "finalPageNo": self.finalPageNo
            , "firstPageNo": self.firstPageNo
            , "num": num
        }
        return result
