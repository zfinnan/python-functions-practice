# function countScores(people) {
#   const scoresObj = {};

#   for (let i = 0; i < people.length; i += 1) {
#     let personObj = people[i];
#     let name = personObj.name;
#     let score = personObj.score;

#     if (scoresObj[name]) {
#       scoresObj[name] += score;
#     } else {
#       scoresObj[name] = score;
#     }
#   }

#   return scoresObj;
# }

def count_scores(people):
    scores_obj = {}
    for i in range(len(people.length)):
        person_obj = people[i]
        name = person_obj.name
        score = person_obj.score

    if scores_obj[name]:
        scores_obj[name] += score
    else:
        scores_obj[name] = score
    
    return scores_obj