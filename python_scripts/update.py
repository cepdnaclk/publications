import requests
import json
import os

# Where the API is available
apiIndex = 'https://api.ce.pdn.ac.lk/publications/v1'

r = requests.get("{0}/all".format(apiIndex))

# Fetch data from the api.ce.pdn.ac.lk
if r.status_code == 200:
    data = json.loads(r.text)

    publications_all = sorted(data, key=lambda k: "{}{}".format(5000-int(k['year']),k["title"]),reverse=False)
    # publications_list = []

    # for pub in publications_all:
    #     filename = pub['api_url'].replace('https://api.ce.pdn.ac.lk', '..') + "index.json"
    #     pub_data = json.load(open(filename, "r"))
    #     author_cards = []

    #     if len(pub_data["authors"]) != len(pub_data["author_info"]):
    #         for aIdx in range(len(pub_data["authors"])):
    #             author_cards.append({
    #                 "name": pub_data["authors"][aIdx],
    #                 "profile": "#",
    #                 "type": "UNDETERMINED"
    #             })
    #     else:
    #         for aIdx in range(len(pub_data["authors"])):
    #             if pub_data["author_info"][aIdx]["type"] == "OUTSIDER":
    #                 author_cards.append({
    #                     "name": pub_data["authors"][aIdx],
    #                     "profile": "#",
    #                     "type": "OUTSIDER"
    #                 })
    #             else:
    #                 author_cards.append({
    #                     "name": pub_data["authors"][aIdx],
    #                     "profile": pub_data["author_info"][aIdx]["profile_url"],
    #                     "type": pub_data["author_info"][aIdx]["type"]
    #                 })

    #     edit_url = pub['api_url'].replace(
    #         "https://api.ce.pdn.ac.lk/", "https://github.com/cepdnaclk/api.ce.pdn.ac.lk/blob/main/") + "index.json"

    #     # Prepare a subset of the publication data
    #     pub_info = {
    #         'title': pub_data['title'],
    #         'venue': pub_data['venue'],
    #         'year': pub_data['year'],
    #         'abstract': pub_data['abstract'],
    #         'authors': pub_data['authors'],
    #         'author_cards': author_cards,
    #         'doi': pub_data['doi'],
    #         'preprint': pub_data['preprint_url'] or "#",
    #         'pdf': pub_data['pdf_url'] or "#",
    #         'presentation': pub_data['presentation_url'] or "#",
    #         'project': pub_data['project_url'] or "#",
    #         'codebase': pub_data['codebase'] or "#",
    #         'researchgroups': pub_data['research_groups'],
    #         'funding': pub_data['funding'],
    #         'tags': pub_data['tags'],
    #         'api_url': pub_data['api_url'],
    #         'edit_url': edit_url
    #     }

    #     print(pub_data['title'])
    #     publications_list.append(temp_pub_info)

    #     tag_dict = {}
    #     if 'tags' in pub_data:
    #         for tag in pub_data['tags']:
    #             if tag != "":
    #                 if tag not in tag_dict:
    #                     tag_dict[tag] = []
    #                 tag_dict[tag].append(pub_info)
    #                 print('  > Tag:', tag)

    #     research_group_dict = {}
    #     if 'research_groups' in pub_data:
    #         for tag in pub_data['research_groups']:
    #             if tag != "":
    #                 if tag not in research_group_dict:
    #                     research_group_dict[tag] = []
    #                 research_group_dict[tag].append(pub_info)
    #                 print('  > Research Group:', tag)

    filename = "../_data/publications.json"
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    with open(filename, "w") as f:
        f.write(json.dumps(publications_all, indent=4))