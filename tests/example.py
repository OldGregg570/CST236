from pywinauto import application

app = application.Application()

app.start('../SharpTona.exe')

app.sharpTona['Question:Edit'].TypeKeys('Who am I?', with_spaces=True)

print app.sharpTona['Ask'].IsEnabled()
print app.sharpTona['Teach'].IsEnabled()
print app.sharpTona['Teach'].IsEnabled()

app.sharpTona['Ask'].Click()

print app.sharpTona['Answer:Edit'].Texts()[0]


app.sharpTona.Close()
