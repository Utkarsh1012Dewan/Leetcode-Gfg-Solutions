/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {
    
    if (s.length != t.length){
        return false
    }
    
    let obj = {};
    for (let i = 0; i < s.length; i++) {
        obj[s[i]] = (obj[s[i]] || 0) + 1;
    }
    for (let i = 0; i < t.length; i++) {
        if (obj.hasOwnProperty(t[i])) {
            obj[t[i]] -= 1;
            if (obj[t[i]] === 0) {
                delete obj[t[i]];
            }
        }
    }
    for (let key in obj) {
        if (obj[key] !== 0) {
            return false;
        }
    }
    return true;
        

    
};