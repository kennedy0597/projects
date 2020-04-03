import socket
import pandas as pd

excel_file = "CompleteDataset.csv"
excel_data = pd.read_csv(excel_file)
df = pd.DataFrame(excel_data)
df1 = df['Name']
df2 = df['Club']
df3 = df['Wage']

df1 = df1.str.replace(r"[^a-zA-Z\d\_\s]+", "")
df2 = df2.str.replace(r"[^a-zA-Z\d\_\s]+", "")
df3 = df3.str.replace(r"[^a-zA-Z\d\_\s]+", "")

df.update(df1)
df.update(df2)
df.update(df3)


def Main():
    # server
    host = "127.0.0.1"
    port = 5000

    s = socket.socket()
    s.bind((host, port))

    s.listen(1)

    # receiving request from client
    content, addr = s.accept()
    print("Connection innitiated from: ", str(addr))
    while True:
        data = str(content.recv(1024).decode('utf-8'))
        if not data:
            break
        print("From connected user: ", data)

        # processing received data @ server
        Test1 = (df["Nationality"] == data)
        test2 = df[Test1]
        test3 = test2[["Name", "Wage", "Potential"]]
        data = str(test3)

        content.send(data.encode("utf-8"))

        # send to client
    content.close()


if __name__ == "__main__":
    Main()
