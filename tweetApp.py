from random import randint

import yaml

import tweepy

API_KEY = 0
API_KEY_SECRET = 1
ACCESS_TOKEN = 2
ACCESS_TOKEN_SECRET = 3
BEARER_TOKEN = 4
CLIENT_ID = 5  # 未使用
CLIENT_SECRET = 6  # 未使用


def main():
    """
    メイン関数

    Returns:
        int: リターンコード
    """
    # 設定ファイルの読み込みを行う
    keys = importKeys()
    if keys is None:
        return 1

    client = tweepy.Client(
        bearer_token=keys[BEARER_TOKEN],
        consumer_key=keys[API_KEY],
        consumer_secret=keys[API_KEY_SECRET],
        access_token=keys[ACCESS_TOKEN],
        access_token_secret=keys[ACCESS_TOKEN_SECRET],
    )

    # ツイートを取得する
    tweetText = createTweet()
    if tweetText is None:
        return 1

    # ツイートする
    try:
        client.create_tweet(text=tweetText)
    except Exception as e:
        print("ツイートに失敗しました。\n" + str(e))
        return 1

    print("つい～としました")
    print("ツイート内容：" + tweetText)
    return 0


def importKeys():
    """
    設定ファイル（keys.yml）を読み込みます

    Returns:
        list: 読み込んだ結果
    """
    try:
        with open("./keys.yml", "r") as f:
            data = yaml.safe_load(f)
            keys = (
                data["API Key"],
                data["API Key Secret"],
                data["Access Token"],
                data["Access Token Secret"],
                data["Bearer Token"],
                # data["Client ID"],
                # data["Client Secret"],
            )
            return keys
    except FileNotFoundError:
        print("設定ファイルが存在しません。")
        return None
    except Exception:
        print("設定ファイルの読み込みでエラーが発生しました。")
        return None


def createTweet():
    """
    tweet_list.txtからランダムで呟く内容を取得します

    Returns:
        String: 呟く文字列
    """
    try:
        with open("./tweet_list.txt", "r", encoding="UTF-8") as tweetTxt:
            tweetList = tweetTxt.read().splitlines()
    except FileNotFoundError:
        print("ツイートリストが存在しません。")
        return None

    maxRowNum = len(tweetList) - 1
    if maxRowNum <= 0:
        print("ツイートリストの中身がありません。")
        return None

    index = randint(0, maxRowNum)
    # print("呟き内容：" + tweetList[index])
    return tweetList[index]


main()
# createTweet()
