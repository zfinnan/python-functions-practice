# function oddRange(end) {
#   const arr = [];

#   for (let i = 1; i <= end; i += 2) {
#       arr.push(i);
#   }

#   return arr;
# }

def odd_range(end):
    arr = []
    for i in range(len(end[::2])):
        arr.append(i)
    return arr