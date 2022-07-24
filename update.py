import argparse
import requests
import datetime
from pytz import timezone 



if __name__=="__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--url", type=str,default="https://api.ce.pdn.ac.lk/publications/v1/all/")
    args.add_argument("--outputFile", type=str,default="index.html")


    args = args.parse_args()

    response = requests.get(args.url)
    JSON = response.json()
    JSON = sorted(JSON, key=lambda k: k['year'],reverse=True)



    outFile = open(args.outputFile, "w")
    outFile.write('''
    <html>
        <head>
            <title>Publications</title>
            <link rel="stylesheet" href="./styles.css">
        </head>
        <body>
            <h1>Publications from the Department of Computer Engineering, University of Peradeniya</h1>
            <hr>

            <ul>
                <li>The source code for this webpage is <a href="https://github.com/cepdnaclk/publications">here</a></li>
                <li>If a publication is missing, please add it using <a href="https://forms.gle/rT6Bt8JPzoMz4qGM9">this</a> form.</li>
                <li>This webpage is based on the University of Peradeniya, Department of Computer Engineering <a href="https://api.ce.pdn.ac.lk/">API</a>.</li>
                <li>If you have any doubts, please reach out to the maintainers listed <a href="https://github.com/orgs/cepdnaclk/teams/admins-cepdnaclk-github-io/members">here</a>. If you are not a member of the Github organization to view that link, please reach out to <a href="https://people.ce.pdn.ac.lk/students/e17/154/">Akila</a>. If everything else fails, reach out to <a href="https://people.ce.pdn.ac.lk/staff/academic/roshan-ragel/">Prof. Roshan Ragel</a>.</li>
            </ul>


            <table>

    ''')
    

    




    for pubIdx in range(len(JSON)):

        outFile.write("<tr>")
        outFile.write("<td style=\"vertical-align:top\">{}. </td><td>".format(pubIdx+1))

        outFile.write("<b>{}</b><br>".format(JSON[pubIdx]["title"]))
        print(len(JSON[pubIdx]["author_info"]))
        print(JSON[pubIdx]["author_info"])
        print(len(JSON[pubIdx]["authors"]))
        print(JSON[pubIdx]["authors"])
        if len(JSON[pubIdx]["authors"]) != len(JSON[pubIdx]["author_info"]):
            outFile.write("<font color=\"red\">Error in author info: Length mismatch. Edit the Json file <a href=\"{}\">here</a>.</font><br>".format(JSON[pubIdx]["api_url"].replace("https://api.ce.pdn.ac.lk/publications/","https://github.com/cepdnaclk/api.ce.pdn.ac.lk/tree/main/publications/")+"index.json"))
 
        outFile.write(", ".join(JSON[pubIdx]["authors"]))
        outFile.write("<br>")
        
        outFile.write(", ".join("<a href=\"{}\">{}</a>".format(aa["profile_url"],aa["name"]) for aa in JSON[pubIdx]["author_info"]))
        outFile.write("<br>")

        outFile.write("<i>{}</i> ({})<br>".format(JSON[pubIdx]["venue"],JSON[pubIdx]["year"]))

        if JSON[pubIdx]["pdf_url"] != "#":
            outFile.write("<a href=\"{}\">PDF</a> | ".format(JSON[pubIdx]["pdf_url"]))
        
        if JSON[pubIdx]["preprint_url"] != "#":
            outFile.write("<a href=\"{}\">Preprint (PDF)</a> | ".format(JSON[pubIdx]["preprint_url"]))

        if JSON[pubIdx]["doi"]!="#":
            outFile.write("<a href=\"https://doi.org/{}\">{}</a> | ".format(JSON[pubIdx]["doi"],JSON[pubIdx]["doi"]))

        outFile.write("<a href=\"{}\">Edit this entry</a>.<br>".format(JSON[pubIdx]["api_url"].replace("https://api.ce.pdn.ac.lk/publications/","https://github.com/cepdnaclk/api.ce.pdn.ac.lk/tree/main/publications/")+"index.json"))

        outFile.write("<br><br>")


        outFile.write("</td></tr>")


        print("Completed publication {} of {} total publications".format(pubIdx+1,len(JSON)))
    outFile.write("</table><br><hr>Last updated: {} (Sri Lanka time)</body></html>".format(datetime.datetime.now(timezone("Asia/Kolkata")).strftime("%Y-%m-%d %H:%M:%S")))
