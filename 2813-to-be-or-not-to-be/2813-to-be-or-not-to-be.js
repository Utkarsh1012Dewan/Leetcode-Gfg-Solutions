/**
 * @param {string} val
 * @return {Object}
 */

const expect = (val) => {
    const throwError = (errorStr) => {throw new Error(errorStr)};
    
    return {
        toBe:    (val2) => val2 === val || throwError('Not Equal'),
        notToBe: (val2) => val2 !== val || throwError('Equal'),
    };
};

// var expect = function(val) {
    
//     return { 
//     function toBe(val1) => {
//         if (val !== val1) throw new Error('Not Equal');
//         else return true
//     }
//     function notToBe(val2) => {
//         if (val === val2) throw new Error("Equal");
//         else return true
//     }}
    
// };

/**
 * expect(5).toBe(5); // true
 * expect(5).notToBe(5); // throws "Equal"
 */