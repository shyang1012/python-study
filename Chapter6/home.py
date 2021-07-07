from flask import Flask, render_template, request, redirect
import os
from Chapter6.Bbs import BbsService

app = Flask(__name__)


def search(dirName):
    try:
        result = []
        filenames = os.listdir(dirName)
        for filename in filenames:
            full_filename = os.path.join(dirName, filename)
            if os.path.isdir(full_filename):
                search(full_filename)
            else:
                ext = os.path.splitext(full_filename)[-1]
                if ext == '.py':
                    result.append(full_filename)
        return result
    except PermissionError:
        pass


@app.route('/')
def home():
    testData = 'testData array'
    dirList = search("/doit")
    return render_template('home.html', testDataHtml=testData, dirList=dirList)


@app.route('/user/<user_name>/<int:user_id>')
def user(user_name, user_id):
    return f"""Hello, {user_name}({user_id})!"""


@app.route("/gugu")
def gugu():
    result = []
    dan = request.args.get('dan', 2, type=int)
    i = 1
    while i < 10:
        result.append(dan * i)
        i += 1
    return render_template('gugu.html', gugu=result, dan=dan)


@app.route("/multiples")
def multiples():
    data = list(range(1, 1000))
    result = 0
    for n in data:
        if n % 3 == 0 or n % 5 == 0:
            result += n
    return render_template('multiples.html', data=data, result=result)


@app.route("/board", methods=['GET', 'POST'])
def bbs_list():
    service = BbsService()
    page = request.args.get('page', 1, type=int)
    searchParam = request.args.get('searchParam', "", type=str)

    article_list = service.getBBSList(searchParam, page)
    paging_info = service.getPagingInfo()
    return render_template('bbs_list.html', article_list=article_list, paging_info=paging_info, page=page,
                           searchParam=searchParam)


@app.route("/board/article/<int:bid>", methods=['GET', 'POST'])
def article(bid):
    service = BbsService()
    article = service.getBBS(bid)
    data = (int(article.get("readCount"))+1, bid)
    service.updateCount(data)
    page = request.args.get('page', 1, type=int)
    searchParam = request.args.get('searchParam', "", type=str)
    return render_template('article.html', article=article, page=page, searchParam=searchParam)


@app.route("/board/writeForm", methods=['GET'])
def writeForm():
    article = {
        "bid": 0
        , "writer": ""
        , "subject": ""
        , "content": ""
        , "regDate": ""
    }
    page = request.args.get('page', 1, type=int)
    searchParam = request.args.get('searchParam', "", type=str)
    return render_template('bbs_form.html', article=article, page=page, searchParam=searchParam, action="save")


@app.route("/board/saveBBS", methods=['POST'])
def save_bbs():
    writer = request.form.get('writer', "", type=str)
    subject = request.form.get('subject', "", type=str)
    content = request.form.get('content', "", type=str)
    service = BbsService()
    data = (writer, subject, content)
    service.saveBBS(data)
    return redirect('/board')


@app.route("/board/updateForm/<int:bid>")
def updateForm(bid):
    service = BbsService()
    article = service.getBBS(bid)
    page = request.args.get('page', 1, type=int)
    searchParam = request.args.get('searchParam', "", type=str)
    return render_template('bbs_form.html', article=article, page=page, searchParam=searchParam, action="update")


@app.route("/board/updateBBS", methods=['POST'])
def update_bbs():
    writer = request.form.get('writer', "", type=str)
    subject = request.form.get('subject', "", type=str)
    content = request.form.get('content', "", type=str)
    bid = request.form.get('bid', "", type=str)
    page = request.form.get('page', 1, type=int)
    searchParam = request.form.get('searchParam', "", type=str)
    service = BbsService()
    data = (writer, subject, content, bid)
    service.updateBBSContent(data)
    return redirect(f"""/board/article/{bid}?page={page}&searchParam={searchParam}""")


@app.route("/board/deleteBBS/<int:bid>", methods=['GET', 'POST'])
def delete_bbs(bid):
    page = request.form.get('page', 1, type=int)
    searchParam = request.form.get('searchParam', "", type=str)
    service = BbsService()
    data = tuple([bid])
    service.deleteBbsContens(data)
    return redirect(f"""/board?page={page}&searchParam={searchParam}""")


if __name__ == '__main__':
    app.run(debug=True)
