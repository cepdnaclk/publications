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
    JSON = sorted(JSON, key=lambda k: "{}{}".format(5000-int(k['year']),k["title"]),reverse=False)
    #Reversse chronological order is how publications are usually sorted on webpages. Sorting by title (lexographic order) is done so it is easy to spot duplicates.



    outFile = open(args.outputFile, "w")
    outFile.write('''
<html>
    <head>
        <meta charset="UTF-8">
        <title>Publications</title>
        <link rel="stylesheet" href="./styles.css">
        <script>
            function highlight(){
                try {
                    var pubBookmarkFormURL=window.location.hash.substr(1);
                    document.getElementsByTagName("tr")[pubBookmarkFormURL].setAttribute("style", "background-color:#ADD8E6");
                }
                catch(err){
                    //Do nothing
                }

            }
        </script>


    </head>
    <body onload="javascript:highlight()">
        <h1>Publications from the Department of Computer Engineering, University of Peradeniya</h1>
        <hr>

        <ul>
            <li>The source code for this webpage is <a href="https://github.com/cepdnaclk/publications">here</a></li>
            <li>If you want to add a missing publication or update an existing publication, please submit it using <a href="https://forms.gle/rT6Bt8JPzoMz4qGM9">this</a> form.</li>
            <li>This webpage is based on the University of Peradeniya, Department of Computer Engineering <a href="https://api.ce.pdn.ac.lk/">API</a>.</li>
            <li>If you have any doubts, please reach out to the maintainers listed <a href="https://github.com/orgs/cepdnaclk/teams/admins-cepdnaclk-github-io/members">here</a>. If you are not a member of the Github organization to view that link, please reach out to <a href="https://people.ce.pdn.ac.lk/students/e17/154/">Akila</a>. If everything else fails, reach out to <a href="https://people.ce.pdn.ac.lk/staff/academic/roshan-ragel/">Prof. Roshan Ragel</a>.</li>
            <li>We are looking for volunteers to make a better looking version of this webpage. If you are interested, please reach out to these <a href="https://projects.ce.pdn.ac.lk/contact/">contacts</a>.</li>
        </ul>


        <table>
''')
    
    # deptAffiliatedPubs = 0
    # externAffiliatedPubs = 0
    # print(JSON[0])
    # for pubIdx in range(len(JSON)):
    #     print(JSON[pubIdx]["is_dept_affiliated"])
    #     if JSON[pubIdx]["is_dept_affiliated"]:
    #         deptAffiliatedPubs+=1
    #     else:
    #         externAffiliatedPubs+=1
    # print(deptAffiliatedPubs,externAffiliatedPubs)



    for pubIdx in range(len(JSON)):
        bookmark = JSON[pubIdx]["doi"].replace("https://doi.org/","").replace("/","_").strip()

        # print(JSON[pubIdx])

        outFile.write("\t\t\t\t<tr id={}>\n".format(bookmark))
        outFile.write("\t\t\t\t\t<td style=\"vertical-align:top\">{}. </td><td>".format(len(JSON) - pubIdx))
        if(not JSON[pubIdx]["is_dept_affiliated"]):
            outFile.write("<font color=\"red\">Not affiliated with the department. This publication will be hidden in the final implementation.</font><br>\n")
        outFile.write("<b>{}</b><br>".format(JSON[pubIdx]["title"]))

        if len(JSON[pubIdx]["authors"]) != len(JSON[pubIdx]["author_info"]):
            outFile.write("\n\t\t\t\t\t"+"<font color=\"red\">Error in author info: Length mismatch. Edit the Json file <a href=\"{}\">here</a>.</font><br>".format(JSON[pubIdx]["api_url"].replace("https://api.ce.pdn.ac.lk/publications/","https://github.com/cepdnaclk/api.ce.pdn.ac.lk/tree/main/publications/")+"index.json"))
        else:
            authorList = []
            for aIdx in range(len(JSON[pubIdx]["authors"])):
                if JSON[pubIdx]["author_info"][aIdx]["type"]=="OUTSIDER":
                    authorList.append(JSON[pubIdx]["authors"][aIdx])
                else:
                    authorList.append("<a href=\"{}\">{}</a>".format(JSON[pubIdx]["author_info"][aIdx]["profile_url"],JSON[pubIdx]["authors"][aIdx]))
        
            outFile.write("\n\t\t\t\t\t"+", ".join(authorList))
            outFile.write("<br>")
        # outFile.write("\n\t\t\t\t\t" + ", ".join(JSON[pubIdx]["authors"]))
        # outFile.write("<br>")
        
        # outFile.write("\n\t\t\t\t\t"+", ".join("<a href=\"{}\">{}</a>".format(aa[1]["profile_url"],aa[0]) for aa in zip(JSON[pubIdx]["authors"],JSON[pubIdx]["author_info"])))
        # outFile.write("<br>")

        outFile.write("\n\t\t\t\t\t"+"<i>{}</i> ({})<br>".format(JSON[pubIdx]["venue"],JSON[pubIdx]["year"]))
        outFile.write("\n\t\t\t\t\t")



        if JSON[pubIdx]["doi"]!="#":
            outFile.write("<a href=\"{}\">DOI</a> | ".format(JSON[pubIdx]["doi"]))

        if JSON[pubIdx]["pdf_url"] != "#":
            outFile.write("<a href=\"{}\">PDF (Open access)</a> | ".format(JSON[pubIdx]["pdf_url"]))
        
        if JSON[pubIdx]["preprint_url"] != "#":
            outFile.write("<a href=\"{}\">PDF (Preprint)</a> | ".format(JSON[pubIdx]["preprint_url"]))

        if JSON[pubIdx]["codebase"] != "#":
            outFile.write("<a href=\"{}\">github</a> | ".format(JSON[pubIdx]["codebase"]))

        if JSON[pubIdx]["project_url"] != "#":
            outFile.write("<a href=\"{}\">Project page</a> | ".format(JSON[pubIdx]["project_url"]))

        if JSON[pubIdx]["presentation_url"] != "#":
            outFile.write("<a href=\"{}\">Presentation</a> | ".format(JSON[pubIdx]["presentation_url"]))
        
        outFile.write("<a href=\"./#{}\">Bookmark</a> | ".format(bookmark))

        outFile.write("<a href=\"{}\">Edit this entry</a>.<br>".format(JSON[pubIdx]["api_url"].replace("https://api.ce.pdn.ac.lk/publications/","https://github.com/cepdnaclk/api.ce.pdn.ac.lk/tree/main/publications/")+"index.json"))

        outFile.write("<br><br>")


        outFile.write("</td></tr>\n")


        print("Completed publication {} of {} total publications".format(pubIdx+1,len(JSON)))
    outFile.write("\t\t\t</table><br><hr>\n\t\t\tLast updated: {} (Sri Lanka time)\n\t</body>\n</html>".format(datetime.datetime.now(timezone("Asia/Kolkata")).strftime("%Y-%m-%d %H:%M:%S")))
