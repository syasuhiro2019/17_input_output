""""
課題

user_data.csv というテキストファイルに記載されている
ユーザー名をすべて出力してください

次のように出力されればok

Ken Tanaka
Tom Ford
Ieyasu Tokugawa
"""


def main():
    with open('user_data.csv', mode='r') as f:
        data = f.read()

        # print(data)

        lines = data.split("\n")

        for line in lines:
            print(line.split(',')[0])


        # line1 = data.split('\n')[0]
        # line2 = data.split('\n')[1]
        # line3 = data.split('\n')[2]
        #
        # print(line1.split(',')[0])
        # print(line2.split(',')[0])
        # print(line3.split(',')[0])


if __name__ == '__main__':
    main()
