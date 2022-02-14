course = {
    "title": "python course",
    "teacher": "ordukhani",
    "time": 8.5,
    "videoCount": 30,
    "tags": ["phthon", "online free pythone"],
    "shortLinl": "toplearn.com/c/o2v3",
    "sessions": [
        {
            "title": "session-1",
            "time": 5
        },
        {
            "title": "session-2",
            "time": 7
        },
        {
            "title": "session-3",
            "time": 10
        }
    ],
    "relatedCourses": [
        {
            "title": "java course",
            "teacher": "Ehsan dehghani",
            "time": 20,
            "videoCount": 42,
            "tags": ["java", "online free java"],
            "shortLinl":"toplearn.com/c/o2v3",
        },
        {"title": ".netcore course",
         "teacher": "hamid ragberag",
         "time": 10,
         "videoCount": 22,
         "tags": [".netcor", "online free .netcore"],
         "shortLinl":"toplearn.com/c/o2v3",
         }


    ]
}
# for related in course["relatedCourses"]:
#     print(related["title"])

total_time = 0

for session in course["sessions"]:
    total_time += session["time"]
print(total_time)