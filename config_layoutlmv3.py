# config.py

folder_path_reg = "vrdu/registration-form/main/pdfs"
dataset_path_reg = "vrdu/registration-form/main/dataset.jsonl.gz"
folder_path_ad = "vrdu/ad-buy-form/main/pdfs"
dataset_path_ad = "vrdu/ad-buy-form/main/dataset.jsonl.gz"

few_shot_examples = {
  "STL": {
    "Amendment": {
      0: [],
      1: [
        {
          "text": "This document is an amendment to the registration statement filed by Japan Trade Center, Los Angeles, with registration number 1833. The amendment is to correct the supplemental statement to provide the recipient of a public relations fee, PressAid Center. The amendment is signed and sworn by Akira Tsutsumi, Director General, on October 1982, and notarized by Robert Pandur.",
          "entities": {
            "file_date": "1982-10-31",
            "foreign_principle_name": "Japan Trade Center, Los Angeles",
            "registrant_name": "PressAid Center",
            "registration_num": "1833",
            "signer_name": "Akira Tsutsumi",
            "signer_title": "Director General"
          }
        }
      ],
      3: [
        {
          "text": "This document is an amendment to the registration statement filed by Japan Trade Center, Los Angeles, with registration number 1833. The amendment is to correct the supplemental statement to provide the recipient of a public relations fee, PressAid Center. The amendment is signed and sworn by Akira Tsutsumi, Director General, on October 1982, and notarized by Robert Pandur.",
          "entities": {
            "file_date": "1982-10-31",
            "foreign_principle_name": "Japan Trade Center, Los Angeles",
            "registrant_name": "PressAid Center",
            "registration_num": "1833",
            "signer_name": "Akira Tsutsumi",
            "signer_title": "Director General"
          }
        },
        {
          "text": "This amendment, filed by Hecht, Spencer & Associates, Inc., with registration number 5451, provides a 10-day notice of change in information as per the Foreign Agents Registration Act. The amendment includes a contract renewal with a foreign principal from April 7, 2012, to March 31, 2013. It is signed by Timothy P. Hecht on May 03, 2012.",
          "entities": {
            "file_date": "2012-05-03",
            "foreign_principle_name": "Foreign Principal (not specified)",
            "registrant_name": "Hecht, Spencer & Associates, Inc.",
            "registration_num": "5451",
            "signer_name": "Timothy P. Hecht",
            "signer_title": "Principal"
          }
        },
        {
          "text": "Crowell & Moring International Ltd., registration number 3988, filed this amendment to include an Exhibit B for the Singapore Trade Development Board. The document details a renewed contract between the registrant and the foreign principal. The amendment is signed by Doral S. Cooper, President, and is notarized.",
          "entities": {
            "file_date": "1992-11-01",
            "foreign_principle_name": "Singapore Trade Development Board",
            "registrant_name": "Crowell & Moring International Ltd.",
            "registration_num": "3988",
            "signer_name": "Doral S. Cooper",
            "signer_title": "President"
          }
        }
      ],
      5: [
        {
          "text": "This document is an amendment to the registration statement filed by Japan Trade Center, Los Angeles, with registration number 1833. The amendment is to correct the supplemental statement to provide the recipient of a public relations fee, PressAid Center. The amendment is signed and sworn by Akira Tsutsumi, Director General, on October 1982, and notarized by Robert Pandur.",
          "entities": {
            "file_date": "1982-10-31",
            "foreign_principle_name": "Japan Trade Center, Los Angeles",
            "registrant_name": "PressAid Center",
            "registration_num": "1833",
            "signer_name": "Akira Tsutsumi",
            "signer_title": "Director General"
          }
        },
        {
          "text": "This amendment, filed by Hecht, Spencer & Associates, Inc., with registration number 5451, provides a 10-day notice of change in information as per the Foreign Agents Registration Act. The amendment includes a contract renewal with a foreign principal from April 7, 2012, to March 31, 2013. It is signed by Timothy P. Hecht on May 03, 2012.",
          "entities": {
            "file_date": "2012-05-03",
            "foreign_principle_name": "Foreign Principal (not specified)",
            "registrant_name": "Hecht, Spencer & Associates, Inc.",
            "registration_num": "5451",
            "signer_name": "Timothy P. Hecht",
            "signer_title": "Principal"
          }
        },
        {
          "text": "Crowell & Moring International Ltd., registration number 3988, filed this amendment to include an Exhibit B for the Singapore Trade Development Board. The document details a renewed contract between the registrant and the foreign principal. The amendment is signed by Doral S. Cooper, President, and is notarized.",
          "entities": {
            "file_date": "1992-11-01",
            "foreign_principle_name": "Singapore Trade Development Board",
            "registrant_name": "Crowell & Moring International Ltd.",
            "registration_num": "3988",
            "signer_name": "Doral S. Cooper",
            "signer_title": "President"
          }
        },
        {
          "text": "Patton, Boggs & Blow, with registration number 2165, filed this amendment to terminate their registration for the Government of Uganda. The document is signed by Timothy J. May, Managing Partner, and notarized in Washington, D.C.",
          "entities": {
            "file_date": "1993-10-12",
            "foreign_principle_name": "Government of Uganda",
            "registrant_name": "Patton, Boggs & Blow",
            "registration_num": "2165",
            "signer_name": "Timothy J. May",
            "signer_title": "Managing Partner"
          }
        },
        {
          "text": "Fleishman-Hillard Inc., with registration number 5801, filed this amendment to notify a change in information regarding a contract with the Social Communication Secretariat of the President of Brazil. The amendment includes a clause on nepotism and extends the contract term until January 16, 2017. Signed by William B. Winkeler, Sr. Vice President, on February 26, 2016.",
          "entities": {
            "file_date": "2016-02-26",
            "foreign_principle_name": "Social Communication Secretariat of the President of Brazil",
            "registrant_name": "Fleishman-Hillard Inc.",
            "registration_num": "5801",
            "signer_name": "William B. Winkeler",
            "signer_title": "Sr. Vice President, Sr. Partner & Corporate Controller"
          }
        }
      ]
    },
    "Dissemination": {
      0: [],
      1: [
        {
          "text": "This dissemination report is filed by JETRO Chicago, registration number 1850. The report describes the transmission of business and economic information on Japanese market entry, titled 'Success in the Making: How Smaller U.S. Companies are Winning New Markets in Japan.' The material was transmitted by mail on November 17, 1993, with a total of 33 copies sent to various states in the Midwest. The report is signed by Minoru Suzuki, Executive Director of Public Affairs.",
          "entities": {
            "file_date": "1993-11-17",
            "foreign_principle_name": "Japan External Trade Organization",
            "registrant_name": "JETRO Chicago",
            "registration_num": "1850",
            "signer_name": "Minoru Suzuki",
            "signer_title": "Executive Director, Public Affairs"
          }
        }
      ],
      3: [
        {
          "text": "This dissemination report is filed by JETRO Chicago, registration number 1850. The report describes the transmission of business and economic information on Japanese market entry, titled 'Success in the Making: How Smaller U.S. Companies are Winning New Markets in Japan.' The material was transmitted by mail on November 17, 1993, with a total of 33 copies sent to various states in the Midwest. The report is signed by Minoru Suzuki, Executive Director of Public Affairs.",
          "entities": {
            "file_date": "1993-11-17",
            "foreign_principle_name": "Japan External Trade Organization",
            "registrant_name": "JETRO Chicago",
            "registration_num": "1850",
            "signer_name": "Minoru Suzuki",
            "signer_title": "Executive Director, Public Affairs"
          }
        },
        {
          "text": "JETRO Atlanta, with registration number 4069, filed this dissemination report detailing the transmission of a newsletter titled 'Focus Japan' (Vol. 22, No. 5, May 1995). The newsletter covers business and lifestyle trends in Japan and was mailed on May 23, 1995. A total of 195 copies were distributed across Alabama, Florida, Georgia, and South Carolina. The report is signed by Shoji Isaki, Executive Director.",
          "entities": {
            "file_date": "1995-05-23",
            "foreign_principle_name": "Japan External Trade Organization",
            "registrant_name": "JETRO Atlanta",
            "registration_num": "4069",
            "signer_name": "Shoji Isaki",
            "signer_title": "Executive Director"
          }
        },
        {
          "text": "This report is submitted by JETRO Chicago, registration number 1850, detailing the dissemination of a newsletter titled 'JETRO Midwest Newsletter' (Vol. 4, No. 1). The material, focused on Japanese business and economy, was mailed on January 14, 1994. A total of 888 copies were sent to several Midwest states. The report is signed by Minoru Suzuki, Executive Director of Public Affairs.",
          "entities": {
            "file_date": "1994-01-20",
            "foreign_principle_name": "Japan External Trade Organization",
            "registrant_name": "JETRO Chicago",
            "registration_num": "1850",
            "signer_name": "Minoru Suzuki",
            "signer_title": "Executive Director, Public Affairs"
          }
        }
      ],
      5: [
        {
          "text": "This dissemination report is filed by JETRO Chicago, registration number 1850. The report describes the transmission of business and economic information on Japanese market entry, titled 'Success in the Making: How Smaller U.S. Companies are Winning New Markets in Japan.' The material was transmitted by mail on November 17, 1993, with a total of 33 copies sent to various states in the Midwest. The report is signed by Minoru Suzuki, Executive Director of Public Affairs.",
          "entities": {
            "file_date": "1993-11-17",
            "foreign_principle_name": "Japan External Trade Organization",
            "registrant_name": "JETRO Chicago",
            "registration_num": "1850",
            "signer_name": "Minoru Suzuki",
            "signer_title": "Executive Director, Public Affairs"
          }
        },
        {
          "text": "JETRO Atlanta, with registration number 4069, filed this dissemination report detailing the transmission of a newsletter titled 'Focus Japan' (Vol. 22, No. 5, May 1995). The newsletter covers business and lifestyle trends in Japan and was mailed on May 23, 1995. A total of 195 copies were distributed across Alabama, Florida, Georgia, and South Carolina. The report is signed by Shoji Isaki, Executive Director.",
          "entities": {
            "file_date": "1995-05-23",
            "foreign_principle_name": "Japan External Trade Organization",
            "registrant_name": "JETRO Atlanta",
            "registration_num": "4069",
            "signer_name": "Shoji Isaki",
            "signer_title": "Executive Director"
          }
        },
        {
          "text": "This report is submitted by JETRO Chicago, registration number 1850, detailing the dissemination of a newsletter titled 'JETRO Midwest Newsletter' (Vol. 4, No. 1). The material, focused on Japanese business and economy, was mailed on January 14, 1994. A total of 888 copies were sent to several Midwest states. The report is signed by Minoru Suzuki, Executive Director of Public Affairs.",
          "entities": {
            "file_date": "1994-01-20",
            "foreign_principle_name": "Japan External Trade Organization",
            "registrant_name": "JETRO Chicago",
            "registration_num": "1850",
            "signer_name": "Minoru Suzuki",
            "signer_title": "Executive Director, Public Affairs"
          }
        },
        {
          "text": "Far East Trade Service, Inc., registration number 2985, filed this report to document the dissemination of trade promotion materials for Taiwan, including 'What You Can Sell to Taiwan' and 'Doing Business with Taiwan.' The materials were distributed by mail and in person in December 1992, totaling 12 copies sent to California and Utah. The report is signed by Robert Y. Wang, Director.",
          "entities": {
            "file_date": "1993-01-04",
            "foreign_principle_name": "Far East Trade Service, Inc., Taipei, Taiwan, R.O.C.",
            "registrant_name": "Far East Trade Service, Inc.",
            "registration_num": "2985",
            "signer_name": "Robert Y. Wang",
            "signer_title": "Director"
          }
        },
        {
          "text": "Kobe Trade Information Office, registration number 2438, filed this report detailing the dissemination of tourist promotion materials titled 'Economic Overview of Kobe.' The materials were sent via mail on December 15, 1992, with one copy transmitted to the State of Washington. The report is signed by Toshiaki Baba, Director.",
          "entities": {
            "file_date": "1992-12-15",
            "foreign_principle_name": "Kobe Municipal Govt.",
            "registrant_name": "Kobe Trade Information Office",
            "registration_num": "2438",
            "signer_name": "Toshiaki Baba",
            "signer_title": "Director"
          }
        }
      ]
    },
    "Short-Form": {
      0: [],
      1: [
        {
          "text": "Jessica Lawrence, an employee of Podesta Group, Inc. (registration number 5926), filed this short-form registration. She is responsible for providing strategic counsel to enhance the image and reputation of the Swiss Confederation, represented by the Swiss Embassy in Washington, among U.S. audiences. Her work includes increasing understanding of Swiss-related issues and promoting Switzerland's positive attributes.",
          "entities": {
            "file_date": "2009-09-25",
            "foreign_principle_name": "The Swiss Confederation, represented by the Swiss Embassy in Washington",
            "registrant_name": "Podesta Group, Inc.",
            "registration_num": "5926",
            "signer_name": "Jessica Lawrence",
            "signer_title": "Consultant"
          }
        }
      ],
      3: [
        {
          "text": "Jessica Lawrence, an employee of Podesta Group, Inc. (registration number 5926), filed this short-form registration. She is responsible for providing strategic counsel to enhance the image and reputation of the Swiss Confederation, represented by the Swiss Embassy in Washington, among U.S. audiences. Her work includes increasing understanding of Swiss-related issues and promoting Switzerland's positive attributes.",
          "entities": {
            "file_date": "2009-09-25",
            "foreign_principle_name": "The Swiss Confederation, represented by the Swiss Embassy in Washington",
            "registrant_name": "Podesta Group, Inc.",
            "registration_num": "5926",
            "signer_name": "Jessica Lawrence",
            "signer_title": "Consultant"
          }
        },
        {
          "text": "Jake Dilemani, a consultant for Mercury Public Affairs, LLC (registration number 6170), filed this short-form registration. He will be providing services related to a Deputy Minister's visit to the U.S. on behalf of the foreign principal Globee. His activities do not include political activities as defined by the Foreign Agents Registration Act.",
          "entities": {
            "file_date": "2016-12-13",
            "foreign_principle_name": "Globee",
            "registrant_name": "Mercury Public Affairs, LLC",
            "registration_num": "6170",
            "signer_name": "Jake Dilemani",
            "signer_title": "Consultant"
          }
        },
        {
          "text": "Samantha Vance, an employee of Daniel J. Edelman, Inc. (registration number 3634), filed this short-form registration. She is responsible for developing and supporting a public relations campaign for the Singapore Economic Development Board to promote Singapore as a global city of innovation and business in North America. Her work is not based solely on services rendered to the foreign principal.",
          "entities": {
            "file_date": "2015-02-09",
            "foreign_principle_name": "Singapore Economic Development Board",
            "registrant_name": "Daniel J. Edelman, Inc.",
            "registration_num": "3634",
            "signer_name": "Samantha Vance",
            "signer_title": "Public Relations"
          }
        }
      ],
      5: [
        {
          "text": "Jessica Lawrence, an employee of Podesta Group, Inc. (registration number 5926), filed this short-form registration. She is responsible for providing strategic counsel to enhance the image and reputation of the Swiss Confederation, represented by the Swiss Embassy in Washington, among U.S. audiences. Her work includes increasing understanding of Swiss-related issues and promoting Switzerland's positive attributes.",
          "entities": {
            "file_date": "2009-09-25",
            "foreign_principle_name": "The Swiss Confederation, represented by the Swiss Embassy in Washington",
            "registrant_name": "Podesta Group, Inc.",
            "registration_num": "5926",
            "signer_name": "Jessica Lawrence",
            "signer_title": "Consultant"
          }
        },
        {
          "text": "Jake Dilemani, a consultant for Mercury Public Affairs, LLC (registration number 6170), filed this short-form registration. He will be providing services related to a Deputy Minister's visit to the U.S. on behalf of the foreign principal Globee. His activities do not include political activities as defined by the Foreign Agents Registration Act.",
          "entities": {
            "file_date": "2016-12-13",
            "foreign_principle_name": "Globee",
            "registrant_name": "Mercury Public Affairs, LLC",
            "registration_num": "6170",
            "signer_name": "Jake Dilemani",
            "signer_title": "Consultant"
          }
        },
        {
          "text": "Samantha Vance, an employee of Daniel J. Edelman, Inc. (registration number 3634), filed this short-form registration. She is responsible for developing and supporting a public relations campaign for the Singapore Economic Development Board to promote Singapore as a global city of innovation and business in North America. Her work is not based solely on services rendered to the foreign principal.",
          "entities": {
            "file_date": "2015-02-09",
            "foreign_principle_name": "Singapore Economic Development Board",
            "registrant_name": "Daniel J. Edelman, Inc.",
            "registration_num": "3634",
            "signer_name": "Samantha Vance",
            "signer_title": "Public Relations"
          }
        },
        {
          "text": "Natalie Gewargis, an employee of Patton Boggs LLP (registration number 2165), filed this short-form registration. She will be providing advice and assistance on U.S.-Georgia bilateral issues to the Government of Georgia. Her activities include counseling and assisting the foreign principal in communicating with U.S. Executive and Legislative Branch officials.",
          "entities": {
            "file_date": "2013-03-04",
            "foreign_principle_name": "Government of Georgia",
            "registrant_name": "Patton Boggs LLP",
            "registration_num": "2165",
            "signer_name": "Natalie Gewargis",
            "signer_title": "Senior Communications Specialist"
          }
        },
        {
          "text": "Parthasarathy Rangarajan, an officer of the Government of India Ministry of Tourism (registration number 2329), filed this short-form registration. He is responsible for promoting tourism by assisting travel trade, airlines, tourism exhibitors, schools, associations, and conferences. His work does not involve political activities as defined by the Foreign Agents Registration Act.",
          "entities": {
            "file_date": "2010-12-02",
            "foreign_principle_name": "Government of India Ministry of Tourism",
            "registrant_name": "India Tourism, New York",
            "registration_num": "2329",
            "signer_name": "Parthasarathy Rangarajan",
            "signer_title": "Assistant Director"
          }
        }
      ]
    }
  },
  "UTL": {
    "Amendment": {
      0: [],
      1: [
        {
          "text": "Zurab Kikvadze, associated with the Commonwealth of Dominica Maritime Registry, Inc. (registration number 5335), submitted a short-form registration statement. He serves as a consultant, providing services related to vessel registration sales and certification, as well as mariner certification for the Commonwealth of Dominica. His activities do not involve political activity as defined by the Foreign Agents Registration Act.",
          "entities": {
            "file_date": "2012-09-27",
            "foreign_principle_name": "Commonwealth of Dominica",
            "registrant_name": "Commonwealth of Dominica Maritime Registry, Inc.",
            "registration_num": "5335",
            "signer_name": "Zurab Kikvadze",
            "signer_title": "Captain"
          }
        }
      ],
      3: [
        {
          "text": "Zurab Kikvadze, associated with the Commonwealth of Dominica Maritime Registry, Inc. (registration number 5335), submitted a short-form registration statement. He serves as a consultant, providing services related to vessel registration sales and certification, as well as mariner certification for the Commonwealth of Dominica. His activities do not involve political activity as defined by the Foreign Agents Registration Act.",
          "entities": {
            "file_date": "2012-09-27",
            "foreign_principle_name": "Commonwealth of Dominica",
            "registrant_name": "Commonwealth of Dominica Maritime Registry, Inc.",
            "registration_num": "5335",
            "signer_name": "Zurab Kikvadze",
            "signer_title": "Captain"
          }
        },
        {
          "text": "Miki Wood, a program coordinator for JETRO San Francisco (registration number 1813), submitted a short-form registration statement. She is responsible for promoting trade, investment, and business between Japanese and American companies on behalf of the Japan External Trade Organization (JETRO), Tokyo. Her work includes providing economic, trade, and business data and information to interested organizations.",
          "entities": {
            "file_date": "2017-04-24",
            "foreign_principle_name": "Japan External Trade Organization (JETRO), Tokyo, Japan",
            "registrant_name": "JETRO, San Francisco",
            "registration_num": "1813",
            "signer_name": "Miki Wood",
            "signer_title": "Program Coordinator"
          }
        },
        {
          "text": "Reinhard Wieck, managing director of Deutsche Telekom, Inc. (registration number 4419), filed a short-form registration statement. He is responsible for monitoring and analyzing legislative actions, administrative policies, and regulatory developments affecting Deutsche Telekom's business activities. His role includes communicating with U.S. Government officials regarding laws, regulations, and policies impacting the telecommunications industry.",
          "entities": {
            "file_date": "2010-05-14",
            "foreign_principle_name": "Deutsche Telekom, Inc.",
            "registrant_name": "Deutsche Telekom, Inc.",
            "registration_num": "4419",
            "signer_name": "Reinhard Wieck",
            "signer_title": "Managing Director"
          }
        }
      ],
      5: [
        {
          "text": "Zurab Kikvadze, associated with the Commonwealth of Dominica Maritime Registry, Inc. (registration number 5335), submitted a short-form registration statement. He serves as a consultant, providing services related to vessel registration sales and certification, as well as mariner certification for the Commonwealth of Dominica. His activities do not involve political activity as defined by the Foreign Agents Registration Act.",
          "entities": {
            "file_date": "2012-09-27",
            "foreign_principle_name": "Commonwealth of Dominica",
            "registrant_name": "Commonwealth of Dominica Maritime Registry, Inc.",
            "registration_num": "5335",
            "signer_name": "Zurab Kikvadze",
            "signer_title": "Captain"
          }
        },
        {
          "text": "Miki Wood, a program coordinator for JETRO San Francisco (registration number 1813), submitted a short-form registration statement. She is responsible for promoting trade, investment, and business between Japanese and American companies on behalf of the Japan External Trade Organization (JETRO), Tokyo. Her work includes providing economic, trade, and business data and information to interested organizations.",
          "entities": {
            "file_date": "2017-04-24",
            "foreign_principle_name": "Japan External Trade Organization (JETRO), Tokyo, Japan",
            "registrant_name": "JETRO, San Francisco",
            "registration_num": "1813",
            "signer_name": "Miki Wood",
            "signer_title": "Program Coordinator"
          }
        },
        {
          "text": "Reinhard Wieck, managing director of Deutsche Telekom, Inc. (registration number 4419), filed a short-form registration statement. He is responsible for monitoring and analyzing legislative actions, administrative policies, and regulatory developments affecting Deutsche Telekom's business activities. His role includes communicating with U.S. Government officials regarding laws, regulations, and policies impacting the telecommunications industry.",
          "entities": {
            "file_date": "2010-05-14",
            "foreign_principle_name": "Deutsche Telekom, Inc.",
            "registrant_name": "Deutsche Telekom, Inc.",
            "registration_num": "4419",
            "signer_name": "Reinhard Wieck",
            "signer_title": "Managing Director"
          }
        },
        {
          "text": "Mark Cowan, a partner at Patton Boggs LLP (registration number 2165), submitted a short-form registration statement. He provides counsel and advice to foreign principals including the Embassy of Ecuador and the Embassy of the People's Republic of China, focusing on bilateral relations with the U.S. Government. His work involves political activities as defined by the Foreign Agents Registration Act.",
          "entities": {
            "file_date": "2009-09-16",
            "foreign_principle_name": "Embassy of Ecuador; Embassy of the People's Republic of China",
            "registrant_name": "Patton Boggs LLP",
            "registration_num": "2165",
            "signer_name": "Mark Cowan",
            "signer_title": "Partner"
          }
        },
        {
          "text": "Hill and Knowlton, Inc., with registration number 3301, submitted a dissemination report detailing the transmission of propaganda materials titled 'Note on Displaced Iraqis' on behalf of the Republic of Turkey. The materials were transmitted via mail from Washington, D.C., to the District of Columbia on June 16, 1992. The total number of copies transmitted was nine.",
          "entities": {
            "file_date": "1992-06-17",
            "foreign_principle_name": "Republic of Turkey",
            "registrant_name": "Hill and Knowlton, Inc.",
            "registration_num": "3301",
            "signer_name": "Gary Hymel",
            "signer_title": "Vice Chairman"
          }
        }
      ]
    },
    "Dissemination": {
      0: [],
      1: [
        {
          "text": "Nancy Smith, a Public Relations Consultant with Burson-Marsteller, LLC (Registration No. 6227), filed a Short Form Registration Statement on behalf of Consejo De Promocion Turistica De Mexico, S.A on 03/20/2017. The services include integrated public relations activities in the United States, such as research, media relations, and stakeholder engagement.",
          "entities": {
            "file_date": "2017-03-20",
            "foreign_principle_name": "Consejo De Promocion Turistica De Mexico, S.A",
            "registrant_name": "Burson-Marsteller, LLC",
            "registration_num": "6227",
            "signer_name": "Nancy Smith",
            "signer_title": "Public Relations Consultant"
          }
        }
      ],
      3: [
        {
          "text": "Nancy Smith, a Public Relations Consultant with Burson-Marsteller, LLC (Registration No. 6227), filed a Short Form Registration Statement on behalf of Consejo De Promocion Turistica De Mexico, S.A on 03/20/2017. The services include integrated public relations activities in the United States, such as research, media relations, and stakeholder engagement.",
          "entities": {
            "file_date": "2017-03-20",
            "foreign_principle_name": "Consejo De Promocion Turistica De Mexico, S.A",
            "registrant_name": "Burson-Marsteller, LLC",
            "registration_num": "6227",
            "signer_name": "Nancy Smith",
            "signer_title": "Public Relations Consultant"
          }
        },
        {
          "text": "The Singapore Economic Development Board (Registration No. 2003) filed an amendment to correct a deficiency related to operational expenses for the period ending August 31, 2006. The amendment details various operational expenses incurred, totaling $1,504,678.19.",
          "entities": {
            "file_date": "2007-02-16",
            "foreign_principle_name": "Singapore Economic Development Board",
            "registrant_name": "Singapore Economic Development Board",
            "registration_num": "2003",
            "signer_name": "Pei-Wei Woo",
            "signer_title": "N/A"
          }
        },
        {
          "text": "Endeavor Law Firm, PC (Registration No. 5934) filed an amendment to correct a deficiency in the supplemental statement for the period ending 11/30/2014. This includes a breakdown of $68,000 spent on professional services provided by Westlaw Legal Research and Cullen Hendrix.",
          "entities": {
            "file_date": "2015-04-10",
            "foreign_principle_name": "N/A",
            "registrant_name": "Endeavor Law Firm, PC",
            "registration_num": "5934",
            "signer_name": "Adam R. Waldman",
            "signer_title": "N/A"
          }
        }
      ],
      5: [
        {
          "text": "Nancy Smith, a Public Relations Consultant with Burson-Marsteller, LLC (Registration No. 6227), filed a Short Form Registration Statement on behalf of Consejo De Promocion Turistica De Mexico, S.A on 03/20/2017. The services include integrated public relations activities in the United States, such as research, media relations, and stakeholder engagement.",
          "entities": {
            "file_date": "2017-03-20",
            "foreign_principle_name": "Consejo De Promocion Turistica De Mexico, S.A",
            "registrant_name": "Burson-Marsteller, LLC",
            "registration_num": "6227",
            "signer_name": "Nancy Smith",
            "signer_title": "Public Relations Consultant"
          }
        },
        {
          "text": "The Singapore Economic Development Board (Registration No. 2003) filed an amendment to correct a deficiency related to operational expenses for the period ending August 31, 2006. The amendment details various operational expenses incurred, totaling $1,504,678.19.",
          "entities": {
            "file_date": "2007-02-16",
            "foreign_principle_name": "Singapore Economic Development Board",
            "registrant_name": "Singapore Economic Development Board",
            "registration_num": "2003",
            "signer_name": "Pei-Wei Woo",
            "signer_title": "N/A"
          }
        },
        {
          "text": "Endeavor Law Firm, PC (Registration No. 5934) filed an amendment to correct a deficiency in the supplemental statement for the period ending 11/30/2014. This includes a breakdown of $68,000 spent on professional services provided by Westlaw Legal Research and Cullen Hendrix.",
          "entities": {
            "file_date": "2015-04-10",
            "foreign_principle_name": "N/A",
            "registrant_name": "Endeavor Law Firm, PC",
            "registration_num": "5934",
            "signer_name": "Adam R. Waldman",
            "signer_title": "N/A"
          }
        },
        {
          "text": "Dickens & Madson Canada, Inc. (Registration No. 6200) filed an amendment to add a new foreign principal as described in the additional Exhibits A and B on 11/07/2014. The amendment includes changes required by Section 2(b) of the Act.",
          "entities": {
            "file_date": "2014-11-10",
            "foreign_principle_name": "N/A",
            "registrant_name": "Dickens & Madson Canada, Inc.",
            "registration_num": "6200",
            "signer_name": "Ari Ben-Menashe",
            "signer_title": "President"
          }
        },
        {
          "text": "Benjamin DeRosa, a Graphic Designer at FTI Consulting (Registration No. 6484), filed a Short Form Registration Statement on behalf of the Ministry of Economy Mexico on 01/29/2018. Services include graphic design support for presentations and printed materials.",
          "entities": {
            "file_date": "2018-01-29",
            "foreign_principle_name": "Ministry of Economy Mexico",
            "registrant_name": "FTI Consulting",
            "registration_num": "6484",
            "signer_name": "Benjamin DeRosa",
            "signer_title": "Graphic Designer"
          }
        }
      ]
    },
    "Short-Form": {
      0: [],
      1: [
        {
          "text": "The Office of the Representative of the Turkish Republic of Northern Cyprus (Registration No. 2619) filed a Dissemination Report on 07/02/1991. The report details the dissemination of books and pamphlets on behalf of the foreign principal during June 1991, primarily via mail to various locations across the United States.",
          "entities": {
            "file_date": "1991-07-02",
            "foreign_principle_name": "Turkish Republic of Northern Cyprus",
            "registrant_name": "Office of the Representative of the Turkish Republic of Northern Cyprus",
            "registration_num": "2619",
            "signer_name": "Osman Ertug",
            "signer_title": "Director"
          }
        }
      ],
      3: [
        {
          "text": "The Office of the Representative of the Turkish Republic of Northern Cyprus (Registration No. 2619) filed a Dissemination Report on 07/02/1991. The report details the dissemination of books and pamphlets on behalf of the foreign principal during June 1991, primarily via mail to various locations across the United States.",
          "entities": {
            "file_date": "1991-07-02",
            "foreign_principle_name": "Turkish Republic of Northern Cyprus",
            "registrant_name": "Office of the Representative of the Turkish Republic of Northern Cyprus",
            "registration_num": "2619",
            "signer_name": "Osman Ertug",
            "signer_title": "Director"
          }
        },
        {
          "text": "Barbados Investment & Development Corp. and Barbados Tourism Authority (Registration No. 1995) filed an Amendment on 07/14/1999. The amendment corrected deficiencies in the Supplemental Statement for the period ending November 1998. An appropriate filing fee of $610 was attached.",
          "entities": {
            "file_date": "1999-07-14",
            "foreign_principle_name": "N/A",
            "registrant_name": "Barbados Investment & Development Corp. and Barbados Tourism Authority",
            "registration_num": "1995",
            "signer_name": "Colene M Clarke",
            "signer_title": "N/A"
          }
        },
        {
          "text": "JETRO, Atlanta (Registration No. 4069) filed a Dissemination Report on 06/14/1995. The report details the dissemination of the 'Tradescope' newsletter, providing news on Japan's import market. A total of 59 copies were transmitted via U.S. Mail to various states, including AL, FL, GA, and SC.",
          "entities": {
            "file_date": "1995-06-14",
            "foreign_principle_name": "Japan External Trade Organization",
            "registrant_name": "JETRO, Atlanta",
            "registration_num": "4069",
            "signer_name": "Shoji Isaki",
            "signer_title": "Executive Director"
          }
        }
      ],
      5: [
        {
          "text": "The Office of the Representative of the Turkish Republic of Northern Cyprus (Registration No. 2619) filed a Dissemination Report on 07/02/1991. The report details the dissemination of books and pamphlets on behalf of the foreign principal during June 1991, primarily via mail to various locations across the United States.",
          "entities": {
            "file_date": "1991-07-02",
            "foreign_principle_name": "Turkish Republic of Northern Cyprus",
            "registrant_name": "Office of the Representative of the Turkish Republic of Northern Cyprus",
            "registration_num": "2619",
            "signer_name": "Osman Ertug",
            "signer_title": "Director"
          }
        },
        {
          "text": "Barbados Investment & Development Corp. and Barbados Tourism Authority (Registration No. 1995) filed an Amendment on 07/14/1999. The amendment corrected deficiencies in the Supplemental Statement for the period ending November 1998. An appropriate filing fee of $610 was attached.",
          "entities": {
            "file_date": "1999-07-14",
            "foreign_principle_name": "N/A",
            "registrant_name": "Barbados Investment & Development Corp. and Barbados Tourism Authority",
            "registration_num": "1995",
            "signer_name": "Colene M Clarke",
            "signer_title": "N/A"
          }
        },
        {
          "text": "JETRO, Atlanta (Registration No. 4069) filed a Dissemination Report on 06/14/1995. The report details the dissemination of the 'Tradescope' newsletter, providing news on Japan's import market. A total of 59 copies were transmitted via U.S. Mail to various states, including AL, FL, GA, and SC.",
          "entities": {
            "file_date": "1995-06-14",
            "foreign_principle_name": "Japan External Trade Organization",
            "registrant_name": "JETRO, Atlanta",
            "registration_num": "4069",
            "signer_name": "Shoji Isaki",
            "signer_title": "Executive Director"
          }
        },
        {
          "text": "Independent Diplomat (Registration No. 5860) filed an Amendment on 04/08/2013. The amendment was made to indicate the acquisition of a new foreign principal and included Exhibit A to register the foreign principal and Exhibit B for the agreement between Independent Diplomat and the foreign principal.",
          "entities": {
            "file_date": "2013-04-08",
            "foreign_principle_name": "N/A",
            "registrant_name": "Independent Diplomat, Inc.",
            "registration_num": "5860",
            "signer_name": "Jennifer Lake",
            "signer_title": "N/A"
          }
        },
        {
          "text": "The Office of Turkish Cypriot Community (Registration No. 2619) filed an Amendment on 12/28/1976. The amendment included changes to the registrant's address and corrections in response to articles published in the Chicago Daily News and the Times Herald Record regarding the Cyprus conflict.",
          "entities": {
            "file_date": "1977-01-01",
            "foreign_principle_name": "Turkish Cypriot Community",
            "registrant_name": "Office of Turkish Cypriot Community",
            "registration_num": "2619",
            "signer_name": "Nail Atalay",
            "signer_title": "Director"
          }
        }
      ]
    }
  }
}

few_shot_examples_ad = {
    'STL': {
        0: [],
        1: [
            {
                "text": "For the advertising campaign of Joyce Beatty, the specified property was WCMH, located at 33096 Collection Center Drive, Chicago, IL 60693. Managed by Hulsen Media Services, the flight duration for this advertisement was from January 27, 2020, to February 4, 2020. One notable line item detailed the airing on WCMH's Local News @ 11p from February 3 to February 9, 2020, costing $650.00, contributing to a gross total of $2,200.00. The product advertised was positioned as a Candidate.",
                "entities": {
                  "advertiser": "Joyce Beatty",
                  "agency": "Hulsen Media Services",
                  "contract_num": "",
                  "flight_from": "01/27/20",
                  "flight_to": "02/04/20",
                  "gross_amount": "$2,200.00",
                  "line_item": [
                    {
                      "channel": "WCMH",
                      "program_desc": "Local News @ 11p",
                      "program_end_date": "02/09/20",
                      "program_start_date": "02/03/20",
                      "sub_amount": "$650.00"
                    }
                  ],
                  "product": "Candidate",
                  "property": "WCMH",
                  "tv_address": "33096 Collection Center Drive, Chicago, IL 60693"
                }

            }

        ],
        3: [
            {
                "text": "The invoice from WOI TV detailed an advertising campaign for Pete Buttigieg during his presidential run, represented by AKPD Message & Media. The campaign aired from December 30, 2019, to January 26, 2020, focusing on the Dr. Phil show during peak viewing times. Key billing details include a primary address at 730 N. Franklin, Suite 404, Chicago, IL 60654, and a gross amount charged of $625.00, encompassing various slots that highlight strategic media placement for a national audience.",
                "entities": {
                  "advertiser": "Pete Buttigieg",
                  "agency": "AKPD Message & Media",
                  "contract_num": "",
                  "flight_from": "12/30/19",
                  "flight_to": "01/26/20",
                  "gross_amount": "$625.00",
                  "line_item": [
                    {
                      "channel": "WOI",
                      "program_desc": "Dr. Phil",
                      "program_end_date": "01/26/20",
                      "program_start_date": "01/20/20",
                      "sub_amount": "$125.00"
                    }
                  ],
                  "product": "President/US/Dem",
                  "property": "WOI TV",
                  "tv_address": "PO Box 744201, Atlanta, GA 30374-4201"
                }

            },
            {
                "text": "A contract for WWJ-TV detailed a series of ads for Peters For Senate, spanning from October 6 to October 12, 2020, managed by Screen Strategies Media. The total campaign worth was $94,700.00, targeting morning and prime time spots across shows like CBS This Morning. The property, located in Southfield, MI, facilitated a robust political campaign focusing on key demographics.",
                "entities": {
                  "advertiser": "Peters For Senate",
                  "agency": "Screen Strategies Media",
                  "contract_num": "",
                  "flight_from": "10/06/20",
                  "flight_to": "10/12/20",
                  "gross_amount": "$94,700.00",
                  "line_item": [
                    {
                      "channel": "WWJ-TV",
                      "program_desc": "CBS This Morning",
                      "program_end_date": "10/12/20",
                      "program_start_date": "10/06/20",
                      "sub_amount": "$1,625.00"
                    }
                  ],
                  "product": "D/SENATE",
                  "property": "WWJ-TV",
                  "tv_address": "26905 West 11 Mile Road, Southfield, MI 48037"
                }

            },
            {
                "text": "An invoice from WTAE in Pittsburgh, PA, billed to Amplify Media, detailed a campaign for AB PAC from April 21 to April 27, 2020. The campaign, costing $44,350.00, included multiple airings on Good Morning America and news segments, ensuring wide exposure across various dayparts. This strategic placement aimed to optimize viewer engagement during significant morning hours.",
                "entities": {
                  "advertiser": "AB PAC",
                  "agency": "Amplify Media",
                  "contract_num": "",
                  "flight_from": "04/21/20",
                  "flight_to": "04/27/20",
                  "gross_amount": "$44,350.00",
                  "line_item": [
                    {
                      "channel": "WTAE",
                      "program_desc": "Good Morning America",
                      "program_end_date": "04/24/20",
                      "program_start_date": "04/21/20",
                      "sub_amount": "$1,300.00"
                    }
                  ],
                  "product": "",
                  "property": "WTAE",
                  "tv_address": "400 Ardmore Blvd., Pittsburgh, PA 15221"
                }

            }
        ],
        5: [
            {
                "text": "KTLM, a Telemundo station in McAllen, TX, managed a campaign for Sergio Munoz Jr., featuring ads specifically during prime news slots such as M-F NOTICIAS 40 5P. Broadcast from February 17 to February 23, 2020, the campaign's gross amount reached $4,720.00. The targeted advertising was designed to resonate with the local Hispanic community, enhancing electoral support.",
                "entities": {
                  "advertiser": "Sergio Munoz Jr",
                  "agency": "",
                  "contract_num": "",
                  "flight_from": "02/17/20",
                  "flight_to": "02/23/20",
                  "gross_amount": "$4,720.00",
                  "line_item": [
                    {
                      "channel": "KTLM",
                      "program_desc": "M-F NOTICIAS 40 5P",
                      "program_end_date": "02/23/20",
                      "program_start_date": "02/17/20",
                      "sub_amount": "$400.00"
                    }
                  ],
                  "product": "TELEMUNDO",
                  "property": "KTLM",
                  "tv_address": "P.O. BOX 419306, Boston, MA 02241-9306"
                }

            },
            {
                "text": "The advertising campaign for Mike Bloomberg 2020, managed by Assembly Media, was detailed in an invoice from WSMV-TV in Nashville, TN. With spots strategically placed in early morning and late-night segments from February 10 to February 14, 2020, the campaign amounted to a total of $9,855.00. This effort aimed to maximize reach during varied viewing times, catering to different audience habits.",
                "entities": {
                  "advertiser": "Mike Bloomberg 2020 Inc",
                  "agency": "Assembly - DNC",
                  "contract_num": "",
                  "flight_from": "02/13/20",
                  "flight_to": "02/14/20",
                  "gross_amount": "$9,855.00",
                  "line_item": [
                    {
                      "channel": "WSMV",
                      "program_desc": "M-F 4a-5a",
                      "program_end_date": "02/14/20",
                      "program_start_date": "02/13/20",
                      "sub_amount": "$30.00"
                    }
                  ],
                  "product": "President",
                  "property": "WSMV-TV NASHVILLE",
                  "tv_address": "5700 Knob Road, Nashville, TN 37209"
                }

            },
            {
                "text": "An invoice from Univision for Mike Bloomberg 2020 highlighted a targeted ad run on KFTU for March 4, 2020. Totaling $60.00, the campaign featured midday slots aiming to capture a diverse audience. Located in Phoenix, AZ, the property facilitated broad exposure, supporting Bloomberg's presidential aspirations through strategic daytime advertising.",
                "entities": {
                  "advertiser": "Mike Bloomberg 2020",
                  "agency": "Assembly Media, Inc.",
                  "contract_num": "",
                  "flight_from": "03/04/20",
                  "flight_to": "03/05/20",
                  "gross_amount": "$60.00",
                  "line_item": [
                    {
                      "channel": "KFTU",
                      "program_desc": "M-F 11a-12p",
                      "program_end_date": "03/04/20",
                      "program_start_date": "03/04/20",
                      "sub_amount": "$20.00"
                    }
                  ],
                  "product": "President",
                  "property": "UNIMAS",
                  "tv_address": "6006 South 30th Street, Phoenix, AZ 85042"
                }

            },
            {
                "text": "Beth Parlato's campaign for Congress in NY CD-27 was detailed in a contract with WUTV in Buffalo-Niagara Falls, NY. Managed by Strategic Media Placement, the campaign ran from April 18 to May 4, 2020, totaling $3,560.00. The advertising focused on evening news segments, leveraging peak viewing times to optimize voter outreach and engagement.",
                "entities": {
                  "advertiser": "Beth Parlato",
                  "agency": "Strategic Media Placement",
                  "contract_num": "26905027",
                  "flight_from": "04/18/20",
                  "flight_to": "05/4/20",
                  "gross_amount": "$3,560.00",
                  "line_item": [
                    {
                      "channel": "WUTV",
                      "program_desc": "2 News On Your Side @ 10P",
                      "program_end_date": "04/30/20",
                      "program_start_date": "04/18/20",
                      "sub_amount": "$160.00"
                    }
                  ],
                  "product": "TV",
                  "property": "WUTV",
                  "tv_address": "125 West 55th St, New York, NY 10019"
                }

            },
            {
                "text": "America First Action Inc.'s campaign managed by Del Ray Media was aired on WGAL_MT in Lancaster, PA, from April 24 to April 30, 2020. The total campaign expenditure was $800.00, with spots strategically placed during the M-SU 10-10:30P segment to maximize exposure during prime time slots, aiming to influence viewer opinions during a critical election period.",
                "entities": {
                  "advertiser": "America First Action Inc.",
                  "agency": "Del Ray Media",
                  "contract_num": "",
                  "flight_from": "04/24/20",
                  "flight_to": "04/30/20",
                  "gross_amount": "$800.00",
                  "line_item": [
                    {
                      "channel": "WGALM",
                      "program_desc": "M-SU 10-10:30P",
                      "program_end_date": "04/26/20",
                      "program_start_date": "04/24/20",
                      "sub_amount": "$400.00"
                    }
                  ],
                  "product": "AMERICA FIRST ACTION",
                  "property": "WGAL_MT",
                  "tv_address": "1300 Columbia Ave, Lancaster, PA 17603"
                }

            }
        ]
    },
    'MTL': {
        0: [],
        1: [
            {
                "text": "This advertising record for WEMT in Tri-Cities, managed by Patty Raettig, encompasses a succinct campaign for Diana Harshbarger, running for Congress. The document, active for the broadcasting months of May to June 2020, details a total of 9 spots, combining shorter and more extended engagements, reflecting a strategic use of peak times to optimize visibility and impact. A budget of $1,230.00 underscores a targeted approach to reach the electorate effectively.",
                "entities": {
                  "advertiser": "Diana Harshbarger-Congress-R",
                  "agency": "Ax Media",
                  "contract_num": "",
                  "flight_from": "05/27/20",
                  "flight_to": "06/03/20",
                  "gross_amount": "$1,230.00",
                  "line_item": [
                    {
                      "channel": "Tri Cities (WEMT)",
                      "program_desc": "FOX-Ultimate Tag, FOX-Mental Samurai, FOX-Labor of Love, FOX-WWE SmackDown Live, News 5 on Fox",
                      "program_end_date": "06/03/20",
                      "program_start_date": "05/27/20",
                      "sub_amount": ""
                    }
                  ],
                  "product": "Political Candidate",
                  "property": "Tri Cities (WEMT)",
                  "tv_address": "101 Lee St, Bristol, VA 24201"
                }
            }
        ],
        3: [
            {
                "text": "Leslie Stoll-Oneill's structured broadcasting strategy through KECI+KCFW Combo for Mike Cooney's gubernatorial bid is laid out in this document. Spanning a concise period in May 2020, the campaign includes 36 spots amounting to $4,110.00. It captures a broad audience through multiple time slots, aiming for maximum exposure during morning hours, with a keen focus on peak viewing times to engage a diverse voter base.",
                "entities": {
                  "advertiser": "Mike Cooney For Governor",
                  "agency": "Screen Strategies Media",
                  "contract_num": "",
                  "flight_from": "05/14/20",
                  "flight_to": "05/14/20",
                  "gross_amount": "$4,110.00",
                  "line_item": [
                    {
                      "channel": "KECI+KCFW Combo",
                      "program_desc": "KECI+KCFW MT TODAY, KECI+KCFW TODAY SHOW, KECI+KCFW KELLY AND RYAN, KECI+KCFW JUDY",
                      "program_end_date": "05/14/20",
                      "program_start_date": "05/14/20",
                      "sub_amount": ""
                    }
                  ],
                  "product": "Political Candidate",
                  "property": "KECI+KCFW Combo",
                  "tv_address": "340 West Main St, Missoula, MT 59802"
                }

            },
            {
                "text": "The advertising invoice for Alex Jenson's City Council campaign, serviced by KDLT, offers a detailed glimpse into a localized strategy with a keen focus on prominent news time slots. The document highlights a week-long run from May 25 to May 31, 2020, with ads strategically placed during the NBC Today Show and evening news, aiming for high-impact visibility with a modest budget of $155.00.",
                "entities": {
                  "advertiser": "Alex Jenson for City Council",
                  "agency": "",
                  "contract_num": "",
                  "flight_from": "05/25/20",
                  "flight_to": "05/31/20",
                  "gross_amount": "$155.00",
                  "line_item": [
                    {
                      "channel": "KDLT",
                      "program_desc": "NBC Today Show, M-F 5p-530p, NBC Nightly News Su",
                      "program_end_date": "05/31/20",
                      "program_start_date": "05/25/20",
                      "sub_amount": ""
                    }
                  ],
                  "product": "Local Political",
                  "property": "KDLT",
                  "tv_address": "325 S 1st Ave Ste 100, Sioux Falls, SD 57104"
                }

            },
            {
                "text": "This detailed contract outlines the advertisement efforts for Shemia Fagan, aspiring for Oregon Secretary of State, with an expansive broadcast plan over nine days in May 2020. Managed by AL Media, the campaign spans various morning and prime time slots on KMTR, marking a strategic endeavor to capture diverse audience segments, with a total expenditure set at a calculated rate for optimum reach.",
                "entities": {
                  "advertiser": "Committee To Elect Shemia Fagan -D",
                  "agency": "AL Media",
                  "contract_num": "",
                  "flight_from": "05/11/20",
                  "flight_to": "05/19/20",
                  "gross_amount": "",
                  "line_item": [
                    {
                      "channel": "KMTR",
                      "program_desc": "TODAY SHOW, NBC-Songland, NBC-The Voice, TODAY SHOW WITH H&J, ELLEN",
                      "program_end_date": "05/19/20",
                      "program_start_date": "05/11/20",
                      "sub_amount": ""
                    }
                  ],
                  "product": "FAGAN FOR OR SEC OF STATE",
                  "property": "KMTR",
                  "tv_address": "3825 International Court, Springfield, OR 97477"
                }

            }
        ],
        5: [
            {
                "text": "Focused on Michael Bloomberg's presidential campaign, this contract covers a detailed strategy implemented over a crucial period leading to the election. Managed by Assembly and aired on WYCW, the strategy encompasses a mix of strategic time slots throughout the day, aimed at maximizing reach across diverse demographics, with a systematic approach to scheduling and rate allocation to optimize campaign impact.",
                "entities": {
                  "advertiser": "Michael Bloomberg 2020",
                  "agency": "Assembly",
                  "contract_num": "",
                  "flight_from": "12/30/19",
                  "flight_to": "02/14/20",
                  "gross_amount": "",
                  "line_item": [
                    {
                      "channel": "WYCW",
                      "program_desc": "",
                      "program_end_date": "02/14/20",
                      "program_start_date": "12/30/19",
                      "sub_amount": ""
                    }
                  ],
                  "product": "MIKE BLOOMBERG 2020",
                  "property": "WYCW",
                  "tv_address": "2960 North Meridian Street, Indianapolis, IN 46208"
                }

            },
            {
                "text": "This document details the advertising strategy for Mike Bloomberg 2020 by Assembly, highlighting a focused ad placement on WAPT. The strategy, running from the end of December 2019 to early January 2020, uses a robust total of 84 spots strategically placed during popular programs to maximize viewer engagement and support for Bloomberg’s campaign, with a total expenditure of $32,550.00.",
                "entities": {
                  "advertiser": "Mike Bloomberg 2020, Inc",
                  "agency": "Assembly",
                  "contract_num": "",
                  "flight_from": "12/30/19",
                  "flight_to": "01/08/20",
                  "gross_amount": "$32,550.00",
                  "line_item": [
                    {
                      "channel": "WAPT",
                      "program_desc": "Good Morning America, Judge Judy, Wheel of Fortune, JEOPARDY!, 20/20",
                      "program_end_date": "01/08/20",
                      "program_start_date": "12/30/19",
                      "sub_amount": ""
                    }
                  ],
                  "product": "MIKE BLOOMBERG 2020 INC",
                  "property": "WAPT",
                  "tv_address": "711 3rd Avenue, New York, NY 10017"
                }

            },
            {
                "text": "The KTXA-TV document outlines an advertising campaign by Vote Vets, spanning a week in February 2020. It showcases an intensive strategy to broadcast ads during popular daytime TV shows, ensuring that messages supporting veterans' issues reach a wide audience. With 31 spots and a detailed timing strategy, the campaign leverages high-traffic time slots to enhance viewer engagement.",
                "entities": {
                  "advertiser": "Vote Vets",
                  "agency": "Waterfront Strategies",
                  "contract_num": "",
                  "flight_from": "02/11/20",
                  "flight_to": "02/17/20",
                  "gross_amount": "$10,250.00",
                  "line_item": [
                    {
                      "channel": "KTXA-TV",
                      "program_desc": "RACHEL RAY, DOCTORS, PEOPLE'S COURT, JUDGE MATHIS, MAKE & MOLLY, 630PM News Replay, JEOPARDY",
                      "program_end_date": "02/17/20",
                      "program_start_date": "02/11/20",
                      "sub_amount": ""
                    }
                  ],
                  "product": "Issue",
                  "property": "KTXA-TV",
                  "tv_address": "5233 Bridge St, Fort Worth, TX 76103"
                }

            },
            {
                "text": "This advertising strategy for Club For Growth Action, executed over a week in late June 2020 on KMBC, employs a diversified slotting approach to maximize reach during critical news hours. This approach ensures optimal exposure for their advocacy messages, with careful planning to pre-empt regular programming when necessary, reflecting a calculated investment in political influence through media.",
                "entities": {
                  "advertiser": "Club For Growth Action",
                  "agency": "Target Enterprises",
                  "contract_num": "",
                  "flight_from": "06/23/20",
                  "flight_to": "06/29/20",
                  "gross_amount": "$12,100.00",
                  "line_item": [
                    {
                      "channel": "KMBC",
                      "program_desc": "First News at 6, Good Morning, 5pm News, 6pm News",
                      "program_end_date": "06/29/20",
                      "program_start_date": "06/23/20",
                      "sub_amount": ""
                    }
                  ],
                  "product": "CLUB FOR GROWTH ACTI",
                  "property": "KMBC",
                  "tv_address": "6455 Winchester Ave, Kansas City, MO 64133-6409"
                }

            },
            {
                "text": "This document offers an in-depth look at Ronnie Chatterji’s campaign ads for a state election, detailing a precise and calculated approach. Managed by GMMB and aired on WFMY, the strategy includes placements in prime morning and evening slots, designed to target key demographic groups during peak viewership times, from February 18 to February 24, 2020, ensuring substantial exposure ahead of the election.",
                "entities": {
                  "advertiser": "Ronnie Chatterji",
                  "agency": "GMMB - Greer Margolis Mitchell / POL",
                  "contract_num": "",
                  "flight_from": "02/18/20",
                  "flight_to": "02/24/20",
                  "gross_amount": "$9,790.00",
                  "line_item": [
                    {
                      "channel": "WFMY",
                      "program_desc": "Local News @ 5a, Local News @ 6a, CBS This Morning, Let's Make a Deal, Price is Right, Local News @ 4p, Local News @ 530p, Wheel of Fortune, LN (M-Su)",
                      "program_end_date": "02/24/20",
                      "program_start_date": "02/18/20",
                      "sub_amount": ""
                    }
                  ],
                  "product": "Candidate",
                  "property": "WFMY",
                  "tv_address": ""
                }

            }
        ]
    },
    'UTL': {
        0: [],
        1: [
            {
                "text": "An advertising contract managed by ASSEMBLY agency for Mike Bloomberg 2020's political campaign lists a total expenditure of $32,550.00. The ads were placed on WAPT station in Jackson, MS, running from December 30, 2019, to January 8, 2020, featuring 84 spots including high-profile programs like Good Morning America and Judge Judy. The aim was broad exposure to boost voter outreach during peak viewing times.",
                "entities": {
                  "advertiser": "Mike Bloomberg 2020",
                  "agency": "ASSEMBLY",
                  "contract_num": "26773404",
                  "flight_from": "12/30/19",
                  "flight_to": "1/8/20",
                  "gross_amount": "$32,550.00",
                  "line_item": [
                    {"channel": "WAPT", "program_desc": "Good Morning America", "program_end_date": "1/6", "program_start_date": "12/30", "sub_amount": "$600.00"},
                    {"channel": "WAPT", "program_desc": "Judge Judy", "program_end_date": "1/6", "program_start_date": "12/30", "sub_amount": "$400.00"}
                  ],
                  "product": "MIKE BLOOMBERG 2020 INC",
                  "property": "KATZ TELEVISION",
                  "tv_address": "711 3rd Avenue, New York, NY 10017"
                }

            }
        ],
        3: [
            {
                "text": "This invoice details an ad campaign for Sima for Texas, managed by Screen Strategies Media on KRIV FOX26. The campaign ran from January 27, 2020, to February 23, 2020, focusing on morning news slots. Total billing amounted to $10,925.00, strategically placing ads to optimize exposure during prime morning hours to target key demographics effectively.",
                "entities": {
                  "advertiser": "Sima for Texas",
                  "agency": "Screen Strategies Media",
                  "contract_num": "951197",
                  "flight_from": "01/27/20",
                  "flight_to": "02/23/20",
                  "gross_amount": "$10,925.00",
                  "line_item": [
                    {"channel": "KRIV FOX26", "program_desc": "Morning News 5a", "program_end_date": "02/23/20", "program_start_date": "02/17/20", "sub_amount": "$325.00"},
                    {"channel": "KRIV FOX26", "program_desc": "Morning News 6a", "program_end_date": "02/23/20", "program_start_date": "02/17/20", "sub_amount": "$650.00"}
                  ],
                  "product": "Sima for Texas",
                  "property": "KRIV",
                  "tv_address": "3733 Collection Center Drive, Chicago, IL 60693"
                }

            },
            {
                "text": "The ad booking for Priorities USA Action via Targeted Platform Media covered political issues aired on WSMH, Flint, from April 21, 2020, to April 27, 2020. Total spots were billed at $450.00, with advertising focused during news segments at 10 PM, aiming to capture a mature audience (A35+) with prime time slots to maximize viewer engagement.",
                "entities":{
                  "advertiser": "Priorities USA Action",
                  "agency": "Targeted Platform Media",
                  "contract_num": "4331120",
                  "flight_from": "04/21/20",
                  "flight_to": "04/27/20",
                  "gross_amount": "$450.00",
                  "line_item": [
                    {"channel": "WSMH", "program_desc": "Fox 66 News At Ten", "program_end_date": "04/27/20", "program_start_date": "04/21/20", "sub_amount": "$450.00"}
                  ],
                  "product": "POLITICAL ISSUE (ns)",
                  "property": "WSMH",
                  "tv_address": "G-3463 W Pierson Rd, Flint, MI 48504"
                }

            },
            {
                "text": "The contract details a political ad campaign for Obama for America by Greer Margolis Mitchell, Burns & Associates, aired on WSYX Columbus, during September 2012. The campaign cost $1,687.00 for spots during prime shows like Law & Order: SVU, aiming to leverage popular TV time slots to enhance campaign visibility and influence.",
                "entities": {
                  "advertiser": "Obama for America",
                  "agency": "Greer Margolis Mitchell, Burns & Associates-Washil",
                  "contract_num": "ECR09807855",
                  "flight_from": "09/06/12",
                  "flight_to": "09/17/12",
                  "gross_amount": "$1,687.00",
                  "line_item": [
                    {"channel": "WSYX", "program_desc": "Law & Order: SVU", "program_end_date": "09/17/12", "program_start_date": "09/10/12", "sub_amount": "$100.00"}
                  ],
                  "product": "POLITICAL CANDIDATE (ns)",
                  "property": "WSYX",
                  "tv_address": "1261 Dublin Road, Columbus, OH 43215"
                }

            }
        ],
        5: [
            {
                "text": "The invoice outlines Teresa Tomlinson for Senate's ad campaign managed by Canal Partners Media. Aired on WGCL Atlanta, the campaign ran from May 26, 2020, to June 1, 2020, costing $5,780.00, featuring spots during CBS This Morning and other key daytime slots to target strategic viewer demographics and optimize campaign reach.",
                "entities": {
                  "advertiser": "Teresa Tomlinson for Senate",
                  "agency": "Canal Partners Media LLC",
                  "contract_num": "1022230",
                  "flight_from": "05/26/20",
                  "flight_to": "06/01/20",
                  "gross_amount": "$5,780.00",
                  "line_item": [
                    {"channel": "WGCL", "program_desc": "CBS This Morning", "program_end_date": "05/26/20", "program_start_date": "05/26/20", "sub_amount": "$70.00"}
                  ],
                  "product": "TOMLINSON FOR SENATE",
                  "property": "WGCL",
                  "tv_address": "425 14th Street NW, Atlanta, GA 30318"
                }

            },
            {
                "text": "This document lists a series of political ads for Nina for PA, managed by Dudley Media, aired on WTAE Pittsburgh in May 2020. The campaign included various time slots across morning shows like Good Morning America and midday news, totaling $3,575.00. The focus was on gaining exposure during high-audience periods to maximize outreach.",
                "entities": {
                  "advertiser": "Nina for PA",
                  "agency": "Dudley Media",
                  "contract_num": "2015092",
                  "flight_from": "05/27/20",
                  "flight_to": "05/28/20",
                  "gross_amount": "$3,575.00",
                  "line_item": [
                    {"channel": "WTAE", "program_desc": "Good Morning America", "program_end_date": "05/27/20", "program_start_date": "05/27/20", "sub_amount": "$350.00"}
                  ],
                  "product": "NINA FOR PA",
                  "property": "WTAE",
                  "tv_address": "400 Ardmore Blvd., Pittsburgh, PA 15221"
                }

            },
            {
                "text": "Claire Chase's political campaign ad details were managed by FlexPoint Media Inc., with ads running on KRQE, Albuquerque, from May 14, 2020, to May 20, 2020. Total expenditure was $11,920.00 with 49 spots aired, including during KRQE News 13 This Morning and Jeopardy, aiming at an adult demographic to optimize voter engagement.",
                "entities": {
                  "advertiser": "Claire Chase - NM",
                  "agency": "FlexPoint Media Inc.",
                  "contract_num": "26917349",
                  "flight_from": "5/14/20",
                  "flight_to": "5/20/20",
                  "gross_amount": "$11,920.00",
                  "line_item": [
                    {"channel": "KRQE", "program_desc": "KRQE News 13 This Morning @6A", "program_end_date": "5/20/20", "program_start_date": "5/14/20", "sub_amount": "$625.00"}
                  ],
                  "product": "NM CD-02 2020",
                  "property": "KRQE",
                  "tv_address": "13 Broadcast Pl, Albuquerque, NM 87104"
                }

            },
            {
                "text": "Tom Steyer 2020's ad campaign was managed through a series of spots on KBCW-TV, San Francisco, on February 24, 2020. With a total cost of $611.00, ads were strategically placed during various dayparts, including midday and early evening, to target diverse demographics effectively during peak viewing times.",
                "entities": {
                  "advertiser": "Tom Steyer 2020",
                  "agency": "n/a",
                  "contract_num": "310013497",
                  "flight_from": "02/24/20",
                  "flight_to": "03/01/20",
                  "gross_amount": "$611.00",
                  "line_item": [
                    {"channel": "KBCW", "program_desc": "M-F 12n-1p", "program_end_date": "03/01/20", "program_start_date": "02/24/20", "sub_amount": "$25.00"}
                  ],
                  "product": "n/a",
                  "property": "KBCW-TV",
                  "tv_address": "P.O.Box 33091, Newark, NJ 07188-0091"
                }

            },
            {
                "text": "Jamie Harrison's Senate campaign involved advertising spots aired on Myrtle Beach WBTW from April 21, 2020, to April 27, 2020. Managed by AL Media, the campaign featured prime time slots on shows like CBS This Morning and The Price Is Right, totaling $24,380.00. The strategic ad placement aimed to maximize reach during peak viewing times to influence potential voters effectively.",
                "entities": {
                  "advertiser": "Jaime Harrison",
                  "agency": "AL Media",
                  "contract_num": "2485488",
                  "flight_from": "04/21/20",
                  "flight_to": "04/27/20",
                  "gross_amount": "$24,380.00",
                  "line_item": [
                    {"channel": "WBTW", "program_desc": "CBS This Morning", "program_end_date": "04/24/20", "program_start_date": "04/21/20", "sub_amount": "$1,200.00"}
                  ],
                  "product": "Jamie Harrison :60",
                  "property": "Myrtle Beach WBTW",
                  "tv_address": "n/a"
                }

            }
        ]
    }
}