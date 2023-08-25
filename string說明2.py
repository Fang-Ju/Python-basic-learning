paragraph2 = """This planet has - or rather had - a problem, which was
this: most of the people living on it were unhappy for pretty much
of the time. Many solutions were suggested for this problem, but
most of these were largely concerned with the movements of small
green pieces of paper, which is odd because on the whole it wasn't
the small green pieces of paper that were unhappy."""

def number_text_in_paragraph (paragraph_, text):
    '''
    :param paragraph_: 請輸入搜尋範圍: 文章
    :param text: 請輸入您要找的 '字串'
    :return: None
    '''

    paragraph = paragraph_    # 拷貝一份文章進行運算
    len_ = len(text)   # 要尋找文字的長度
    n = 0
    while paragraph.find(text) != -1:  # 如果搜尋不到您要的答案就離開迴圈
        ans = paragraph.find(text)   # 要搜尋的文字
        paragraph = paragraph[ans+len_:]  
        n += 1

    print(n)

    return None

number_text_in_paragraph (paragraph2, 'of')
