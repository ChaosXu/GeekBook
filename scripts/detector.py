from pyPdf import PdfFileReader
import glob

if __name__ == "__main__":
    f = open("./damaged.txt","a+");
    books = glob.glob("./books/*/*.pdf")
    for book in books:
        # print book
        try:
            mypdf = PdfFileReader(file(book, 'rb'))
        except:
            print 'invalid pdf >',book
            #write to file
            f.write(book+'\n')
    f.close()
