

function e(val) {


    //c(input);
    var perc_array = input.split("%");
    //c(perc_array);
    var l = perc_array.length;

    if (l <= 1) {
        e1();//this line writes "error"when more than 1 % signs are written in display
    } else if (l === 2 || l === 2) {
        //It's a percentage
        //TODO
        var from_perc = perc_array[0];
        var to_perc = perc_array[1];
        //c(to_perc);
        var result = (to_perc / 100) * from_perc;
        //these lines declare the variables.Then it Does           the the formula of percent  
        c(result);//this prints the result
    } else {
        c('Error');
    }

}

var abc = "0";
var def = 0;
var ghi = 0;
var jkl = 3;
var mno = 0;
var decimal = 0;
var enter = "";
function memory(operator) {
    document.pqr.stu.focus();
    if (operator == 1) {		// MS 
        document.pqr.mem.value = document.pqr.resultant.value;
    }
    else if (operator == 2) {	// MR
        var mem = document.pqr.mem.value;
        if (mem == 0 || chracter(mem.charAt(0))) { mem = "" };
        document.pqr.stu.value += mem;
    }
    else if (operator == 3) {	// CLS
        if (document.pqr.stu.value == "") {
            document.pqr.resultant.value = "";
        }
        else {
            document.pqr.stu.value = "";
        }
    }
}
function display(xyz) {
    if (xyz == "")
    { document.pqr.stu.focus() }
    else
    { document.pqr.resultant.select() }
}
function cdef(xyz) {
    document.pqr.stu.focus();
    document.pqr.stu.value += xyz;
}
function factorial(n) {
    if ((n == 0) || (n == 1)) {
        return 1;
    }
    else {
        var opqrst = (n * factorial(n - 1));
        return opqrst;
    }
}
function chracter(valuer) {
    var chracter = "(ABCDEFGHIKLMNOPRSTUVWXYZ";
    for (var i = 0; i < chracter.length; i++)
        if (valuer == chracter.charAt(i)) { return true } { return false }
}
function ghij(klmn) {
    var qrstu = "";
    var mem = 0;
    if (klmn >= 1) {
        if (document.pqr.stu.value == "") {
            abc = document.pqr.resultant.value;
        }
        else {
            abc = document.pqr.stu.value;
            if (resultant(abc.charAt(0))) {
                abc = document.pqr.resultant.value + abc;
            }
        }
    }
    for (var i = 0; i < abc.length; i++) {
        if (abc.charAt(i) == ",") { qrstu += "." }
        else if (abc.charAt(i) == " ") { }
        else { qrstu += abc.charAt(i) }
    }
    if (operator(abc.charAt(abc.length - 1))) { return false };
    qrstu = eval("1*" + qrstu);
    if (klmn > 1) {
        qrstu = mathcalc(klmn, qrstu);
    }
    document.pqr.oldresultant.value = qrstu;
    result(qrstu);
    document.pqr.stu.value = "";
    document.pqr.stu.focus();
}
function mathcalc(klmn, mno) {
    with (Math) {
        if (klmn == 2) {
            mno = pow(mno, 2);
        }
        else if (klmn == 3) {
            mno = sqrt(mno);
        }
        else if (klmn == 4) {
            mno = -mno;
        }
        else if (klmn == 5) {
            mno = log(mno);
        }
        else if (klmn == 6) {
            mno = pow(E, mno);
        }
        else if (klmn == 7) {
            mno = 1 / mno;
        }
        else if (klmn == 8) {
            mno = log(mno) / LN10;
        }
        else if (klmn == 9) {
            mno = pow(10, mno);
        }
        else if (klmn >= 10 && klmn <= 12) {
            if (klmn == 10) {
                mno = atan(mno);
            }
            else if (klmn == 11) {
                mno = acos(mno);
            }
            else if (klmn == 12) {
                mno = asin(mno);
            }
            if (document.pqr.vwxyz[1].checked) { mno = (mno * 180) / PI }
        }
        else if (klmn >= 14 && klmn <= 16) {
            if (document.pqr.vwxyz[1].checked)
            { radian = (mno / 180) * PI }
            else
            { radian = mno };
            if (klmn == 14) {
                mno = tan(radian);
            }
            else if (klmn == 15) {
                mno = cos(radian);
            }
            else if (klmn == 16) {
                mno = sin(radian);
            }
        }
        else if (klmn == 17) {
            mno = mno / 100;
        }
        else if (klmn == 18) {
            mno = mno / 1000000;
        }
        else if (klmn == 20) {
            mno = factorial(mno);
        }
        else if (klmn == 21) {
            jkl = prompt("Kindly enter exponent", 3);
            mno = pow(mno, jkl);
        }
        else if (klmn == 22) {
            jkl = prompt("Kindly enter root", 3);
            mno = pow(mno, (1 / jkl));
        }
        return mno;
    }
}
function validatenum(data, e) {
    if (data.match(/^[a-zA-Z]+$/)) {
        document.getElementById('stu').value = "";
        return false;
    }
    else {
        runScript(e);
        return true;
    }
}
function result(eabc) {
    decimal = parseFloat(document.pqr.xyzab.options[document.pqr.xyzab.selectedIndex].value);
    var strabc = eabc + " ";
    if (strabc.charAt(0) == ".") { strabc = "0" + strabc };
    var intabc = strabc.length - 1;
    decklmn(strabc);
    if (intabc > 16 && ghi == -1) {
        if (decimal == -1) { decimal = 14 };
        strabc = xyzab(strabc.substring(0, intabc)) + " ";
        intabc = strabc.length - 1;
        decklmn(strabc);
    }
    if (decimal >= 0 && decimal != 14) {
        if (def > 0) {
            var opqrst = xyzab(strabc.substring(0, intabc));
        }
        else {
            eabc = strabc.substring(0, intabc);
            if (decimal > 0) {
                eabc += ".";
                for (var n = 0; n < decimal; n++) {
                    eabc += "0";
                }
            }
            var opqrst = eabc
        }
    }
    else {
        decimal = 14;
        var opqrst = xyzab(strabc)
    }
    if (opqrst.charAt(0) == ".") { opqrst = "0" + opqrst };
    document.pqr.resultant.value = opqrst;
}
function decklmn(data1) {
    def = 0;
    ghi = 0;
    def = data1.indexOf(".");
    ghi = data1.indexOf("e");
}
function resultant(valuer) {
    var resultant = "*/+";
    for (var i = 0; i < resultant.length; i++)
        if (valuer == resultant.charAt(i)) { return true }
    return false;
}
function xyzab(data1) {
    with (Math) {
        if (ghi == -1) {
            var value = def;
            if (value == -1) { value = data1.length };
            var value1 = "";
            if (value > 16) {
                var value2 = round(data1 * pow(10, 18)) + " ";
                var value3 = value2.indexOf("e");
                var valuek = (value2.substring(0, value3));
                valuek = round(valuek * pow(10, 15)) / pow(10, 15) + " ";
                value1 = (value2.substring(value3 + 2, value2.length - 1));
                value1 = "e+" + (value1 - 18);
            }
            else {
                var valuek = round(data1 * pow(10, decimal)) / pow(10, decimal) + " "
            }
        }
        else {
            var valuek = data1.substring(0, ghi);
            var value1 = data1.substring(ghi, data1.length);
            valuek = round(valuek * pow(10, decimal)) / pow(10, decimal) + " ";
        }

        valuek = valuek.substring(0, valuek.length - 1);
        if (valuek.charAt(0) == ".") { valuek = "0" + valuek };
        if (decimal < 14) {
            if (valuek.indexOf(".") == -1 && decimal != 0) { valuek += "." };
            var nula = (def + decimal) - (valuek.length - 1);
            if (nula > 0 && decimal > 0) {
                for (var n = 0; n < nula; n++) {
                    valuek += "0";
                }
            }
        }
        return (valuek + " " + value1)
    }
}
function operator(valuer) {
    var dashop = "*/+-";
    for (var i = 0; i < dashop.length; i++)
        if (valuer == dashop.charAt(i)) { return true }
    return false
}
function backspace() {
    var input = document.getElementById('stu').value;
    var out = input.substring(0, input.length - 1)
    document.getElementById('stu').value = out;
}
function runScript(e) {
    if (e.keyCode == 13) {
        ghij(1);
    }
}
