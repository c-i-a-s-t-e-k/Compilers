
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'nonassocIFXnonassocELSEleftDOTADDDOTSUBleftADDMINUSleftDOTMULDOTDIVIDEleftDIVIDEMULrightUMINUSADD ADDASSIGN BREAK CONTINUE DIVASSIGN DIVIDE DOTADD DOTDIVIDE DOTMUL DOTSUB ELSE EQ EYE FLOAT FOR GREATER GREATEREQ ID IF INTNUM LESS LESSEQ MINUS MUL MULASSIGN NOTEQ ONES PRINT RETURN STRING SUBASSIGN WHILE ZEROSprogram : instructions_optinstructions_opt : instructions instructions_opt : instructions : instructions instruction instructions : instruction instruction : assignment \n                    | if_stmt\n                    | loops\n                    | break\n                    | continue \n                    | return_expr \';\'instruction : PRINT create_stmt \';\'instruction : \'{\' instructions \'}\'continue : CONTINUE \';\'break : BREAK \';\'id_change : ID \n                    | ID \'[\' expression \',\' expression \']\'\n                    | ID \'[\' expression \']\'assignment : id_change \'=\' expression \';\'\n                    | id_change ADDASSIGN expression \';\'\n                    | id_change SUBASSIGN expression \';\'\n                    | id_change MULASSIGN expression \';\'\n                    | id_change DIVASSIGN expression \';\'\n                    | id_change \'=\' id_change \';\'\n                    | id_change ADDASSIGN id_change \';\'\n                    | id_change SUBASSIGN id_change \';\'\n                    | id_change MULASSIGN id_change \';\'\n                    | id_change DIVASSIGN id_change \';\'expression : expression ADD expression\n                    | expression MINUS expression\n                    | expression MUL expression\n                    | expression DIVIDE expressionexpression : MINUS expression %prec UMINUSexpression : ID "\'"expression : expression DOTADD expression\n                    | expression DOTSUB expression\n                    | expression DOTMUL expression\n                    | expression DOTDIVIDE expressionexpression : matrix_expression\n                    | matrix_create\n                    | vector_createexpression : INTNUMexpression : FLOATexpression : IDmatrix_expression : ZEROS \'(\' expression \')\' matrix_expression : ONES \'(\' expression \')\' matrix_expression : EYE \'(\' expression \')\' matrix_create : \'[\' matrix_rows \']\'vector_create : \'[\' vector_elems \']\'vector_elems : expression \',\' vector_elems\n                    | expressionmatrix_rows : \'[\' matrix_elems \']\' \',\' matrix_rows\n                    | \'[\' matrix_elems \']\'matrix_elems : expression \',\' matrix_elems\n                    | expressioncondition : expression GREATER expression\n                    | expression LESS expression\n                    | expression GREATEREQ expression\n                    | expression LESSEQ expression\n                    | expression NOTEQ expression\n                    | expression EQ expressionif_stmt : IF \'(\' condition \')\' instruction %prec IFX\n                | IF \'(\' condition \')\' instruction ELSE instruction\n                create_stmt : p_print_listp_print_list : STRING p_print_list : p_print_list \',\' expression\n                    | expressionloops : while_l\n                | for_lwhile_l : WHILE "(" condition ")" instructionfor_l : FOR ID "=" expression ":" expression instructionreturn_expr : RETURN\n                    | RETURN expression'
    
_lr_action_items = {'$end':([0,1,2,3,4,5,6,7,8,9,15,16,23,24,47,48,53,72,106,107,108,109,110,111,112,113,114,115,133,141,150,151,],[-3,0,-1,-2,-5,-6,-7,-8,-9,-10,-68,-69,-4,-11,-15,-14,-12,-13,-24,-19,-25,-20,-26,-21,-27,-22,-28,-23,-62,-70,-63,-71,]),'PRINT':([0,3,4,5,6,7,8,9,12,15,16,23,24,30,31,32,33,34,35,40,47,48,53,63,64,72,90,91,92,93,94,95,96,97,103,104,106,107,108,109,110,111,112,113,114,115,116,125,127,128,129,133,141,145,147,150,151,],[11,11,-5,-6,-7,-8,-9,-10,11,-68,-69,-4,-11,-44,-39,-40,-41,-42,-43,11,-15,-14,-12,-33,-34,-13,-29,-30,-31,-32,-35,-36,-37,-38,-48,-49,-24,-19,-25,-20,-26,-21,-27,-22,-28,-23,11,11,-45,-46,-47,-62,-70,11,11,-63,-71,]),'{':([0,3,4,5,6,7,8,9,12,15,16,23,24,30,31,32,33,34,35,40,47,48,53,63,64,72,90,91,92,93,94,95,96,97,103,104,106,107,108,109,110,111,112,113,114,115,116,125,127,128,129,133,141,145,147,150,151,],[12,12,-5,-6,-7,-8,-9,-10,12,-68,-69,-4,-11,-44,-39,-40,-41,-42,-43,12,-15,-14,-12,-33,-34,-13,-29,-30,-31,-32,-35,-36,-37,-38,-48,-49,-24,-19,-25,-20,-26,-21,-27,-22,-28,-23,12,12,-45,-46,-47,-62,-70,12,12,-63,-71,]),'IF':([0,3,4,5,6,7,8,9,12,15,16,23,24,30,31,32,33,34,35,40,47,48,53,63,64,72,90,91,92,93,94,95,96,97,103,104,106,107,108,109,110,111,112,113,114,115,116,125,127,128,129,133,141,145,147,150,151,],[14,14,-5,-6,-7,-8,-9,-10,14,-68,-69,-4,-11,-44,-39,-40,-41,-42,-43,14,-15,-14,-12,-33,-34,-13,-29,-30,-31,-32,-35,-36,-37,-38,-48,-49,-24,-19,-25,-20,-26,-21,-27,-22,-28,-23,14,14,-45,-46,-47,-62,-70,14,14,-63,-71,]),'BREAK':([0,3,4,5,6,7,8,9,12,15,16,23,24,30,31,32,33,34,35,40,47,48,53,63,64,72,90,91,92,93,94,95,96,97,103,104,106,107,108,109,110,111,112,113,114,115,116,125,127,128,129,133,141,145,147,150,151,],[17,17,-5,-6,-7,-8,-9,-10,17,-68,-69,-4,-11,-44,-39,-40,-41,-42,-43,17,-15,-14,-12,-33,-34,-13,-29,-30,-31,-32,-35,-36,-37,-38,-48,-49,-24,-19,-25,-20,-26,-21,-27,-22,-28,-23,17,17,-45,-46,-47,-62,-70,17,17,-63,-71,]),'CONTINUE':([0,3,4,5,6,7,8,9,12,15,16,23,24,30,31,32,33,34,35,40,47,48,53,63,64,72,90,91,92,93,94,95,96,97,103,104,106,107,108,109,110,111,112,113,114,115,116,125,127,128,129,133,141,145,147,150,151,],[18,18,-5,-6,-7,-8,-9,-10,18,-68,-69,-4,-11,-44,-39,-40,-41,-42,-43,18,-15,-14,-12,-33,-34,-13,-29,-30,-31,-32,-35,-36,-37,-38,-48,-49,-24,-19,-25,-20,-26,-21,-27,-22,-28,-23,18,18,-45,-46,-47,-62,-70,18,18,-63,-71,]),'RETURN':([0,3,4,5,6,7,8,9,12,15,16,23,24,30,31,32,33,34,35,40,47,48,53,63,64,72,90,91,92,93,94,95,96,97,103,104,106,107,108,109,110,111,112,113,114,115,116,125,127,128,129,133,141,145,147,150,151,],[19,19,-5,-6,-7,-8,-9,-10,19,-68,-69,-4,-11,-44,-39,-40,-41,-42,-43,19,-15,-14,-12,-33,-34,-13,-29,-30,-31,-32,-35,-36,-37,-38,-48,-49,-24,-19,-25,-20,-26,-21,-27,-22,-28,-23,19,19,-45,-46,-47,-62,-70,19,19,-63,-71,]),'ID':([0,3,4,5,6,7,8,9,11,12,15,16,19,22,23,24,29,30,31,32,33,34,35,39,40,41,42,43,44,45,46,47,48,50,51,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,72,88,90,91,92,93,94,95,96,97,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,125,127,128,129,131,133,141,142,145,147,148,150,151,153,],[20,20,-5,-6,-7,-8,-9,-10,30,20,-68,-69,30,52,-4,-11,30,-44,-39,-40,-41,-42,-43,30,20,75,75,75,75,75,30,-15,-14,30,30,-12,30,30,30,30,30,30,30,30,30,-33,-34,30,30,30,30,-13,30,-29,-30,-31,-32,-35,-36,-37,-38,-48,-49,30,-24,-19,-25,-20,-26,-21,-27,-22,-28,-23,20,30,30,30,30,30,30,30,20,-45,-46,-47,30,-62,-70,30,20,20,30,-63,-71,30,]),'WHILE':([0,3,4,5,6,7,8,9,12,15,16,23,24,30,31,32,33,34,35,40,47,48,53,63,64,72,90,91,92,93,94,95,96,97,103,104,106,107,108,109,110,111,112,113,114,115,116,125,127,128,129,133,141,145,147,150,151,],[21,21,-5,-6,-7,-8,-9,-10,21,-68,-69,-4,-11,-44,-39,-40,-41,-42,-43,21,-15,-14,-12,-33,-34,-13,-29,-30,-31,-32,-35,-36,-37,-38,-48,-49,-24,-19,-25,-20,-26,-21,-27,-22,-28,-23,21,21,-45,-46,-47,-62,-70,21,21,-63,-71,]),'FOR':([0,3,4,5,6,7,8,9,12,15,16,23,24,30,31,32,33,34,35,40,47,48,53,63,64,72,90,91,92,93,94,95,96,97,103,104,106,107,108,109,110,111,112,113,114,115,116,125,127,128,129,133,141,145,147,150,151,],[22,22,-5,-6,-7,-8,-9,-10,22,-68,-69,-4,-11,-44,-39,-40,-41,-42,-43,22,-15,-14,-12,-33,-34,-13,-29,-30,-31,-32,-35,-36,-37,-38,-48,-49,-24,-19,-25,-20,-26,-21,-27,-22,-28,-23,22,22,-45,-46,-47,-62,-70,22,22,-63,-71,]),'}':([4,5,6,7,8,9,15,16,23,24,40,47,48,53,72,106,107,108,109,110,111,112,113,114,115,133,141,150,151,],[-5,-6,-7,-8,-9,-10,-68,-69,-4,-11,72,-15,-14,-12,-13,-24,-19,-25,-20,-26,-21,-27,-22,-28,-23,-62,-70,-63,-71,]),'ELSE':([5,6,7,8,9,15,16,24,47,48,53,72,106,107,108,109,110,111,112,113,114,115,133,141,150,151,],[-6,-7,-8,-9,-10,-68,-69,-11,-15,-14,-12,-13,-24,-19,-25,-20,-26,-21,-27,-22,-28,-23,145,-70,-63,-71,]),';':([10,17,18,19,25,26,27,28,30,31,32,33,34,35,49,63,64,73,74,75,76,77,78,79,80,81,82,83,89,90,91,92,93,94,95,96,97,103,104,124,127,128,129,146,],[24,47,48,-72,53,-64,-65,-67,-44,-39,-40,-41,-42,-43,-73,-33,-34,106,107,-16,108,109,110,111,112,113,114,115,-66,-29,-30,-31,-32,-35,-36,-37,-38,-48,-49,-18,-45,-46,-47,-17,]),'STRING':([11,],[27,]),'MINUS':([11,19,28,29,30,31,32,33,34,35,39,41,42,43,44,45,46,49,50,51,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,71,74,75,77,79,81,83,85,86,88,89,90,91,92,93,94,95,96,97,98,99,100,102,103,104,105,117,118,119,120,121,122,123,126,127,128,129,131,134,135,136,137,138,139,140,142,147,148,152,153,],[29,29,56,29,-44,-39,-40,-41,-42,-43,29,29,29,29,29,29,29,56,29,29,29,29,29,29,29,29,29,29,29,-33,-34,29,29,29,29,56,56,-44,56,56,56,56,56,56,29,56,-29,-30,-31,-32,56,56,-37,-38,56,56,56,56,-48,-49,29,29,29,29,29,29,29,29,56,-45,-46,-47,29,56,56,56,56,56,56,56,29,56,29,56,29,]),'INTNUM':([11,19,29,39,41,42,43,44,45,46,50,51,54,55,56,57,58,59,60,61,62,65,66,67,68,88,105,117,118,119,120,121,122,123,131,142,148,153,],[34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,]),'FLOAT':([11,19,29,39,41,42,43,44,45,46,50,51,54,55,56,57,58,59,60,61,62,65,66,67,68,88,105,117,118,119,120,121,122,123,131,142,148,153,],[35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,]),'ZEROS':([11,19,29,39,41,42,43,44,45,46,50,51,54,55,56,57,58,59,60,61,62,65,66,67,68,88,105,117,118,119,120,121,122,123,131,142,148,153,],[36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,]),'ONES':([11,19,29,39,41,42,43,44,45,46,50,51,54,55,56,57,58,59,60,61,62,65,66,67,68,88,105,117,118,119,120,121,122,123,131,142,148,153,],[37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,]),'EYE':([11,19,29,39,41,42,43,44,45,46,50,51,54,55,56,57,58,59,60,61,62,65,66,67,68,88,105,117,118,119,120,121,122,123,131,142,148,153,],[38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,]),'[':([11,19,20,29,39,41,42,43,44,45,46,50,51,54,55,56,57,58,59,60,61,62,65,66,67,68,75,88,105,117,118,119,120,121,122,123,131,142,143,148,153,],[39,39,50,39,68,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,68,50,39,39,39,39,39,39,39,39,39,39,39,148,39,39,]),'=':([13,20,52,124,146,],[41,-16,88,-18,-17,]),'ADDASSIGN':([13,20,124,146,],[42,-16,-18,-17,]),'SUBASSIGN':([13,20,124,146,],[43,-16,-18,-17,]),'MULASSIGN':([13,20,124,146,],[44,-16,-18,-17,]),'DIVASSIGN':([13,20,124,146,],[45,-16,-18,-17,]),'(':([14,21,36,37,38,],[46,51,65,66,67,]),',':([26,27,28,30,31,32,33,34,35,63,64,71,86,89,90,91,92,93,94,95,96,97,102,103,104,127,128,129,130,152,],[54,-65,-67,-44,-39,-40,-41,-42,-43,-33,-34,105,123,-66,-29,-30,-31,-32,-35,-36,-37,-38,131,-48,-49,-45,-46,-47,143,153,]),'ADD':([28,30,31,32,33,34,35,49,63,64,71,74,75,77,79,81,83,85,86,89,90,91,92,93,94,95,96,97,98,99,100,102,103,104,126,127,128,129,134,135,136,137,138,139,140,147,152,],[55,-44,-39,-40,-41,-42,-43,55,-33,-34,55,55,-44,55,55,55,55,55,55,55,-29,-30,-31,-32,55,55,-37,-38,55,55,55,55,-48,-49,55,-45,-46,-47,55,55,55,55,55,55,55,55,55,]),'MUL':([28,30,31,32,33,34,35,49,63,64,71,74,75,77,79,81,83,85,86,89,90,91,92,93,94,95,96,97,98,99,100,102,103,104,126,127,128,129,134,135,136,137,138,139,140,147,152,],[57,-44,-39,-40,-41,-42,-43,57,-33,-34,57,57,-44,57,57,57,57,57,57,57,57,57,-31,-32,57,57,57,57,57,57,57,57,-48,-49,57,-45,-46,-47,57,57,57,57,57,57,57,57,57,]),'DIVIDE':([28,30,31,32,33,34,35,49,63,64,71,74,75,77,79,81,83,85,86,89,90,91,92,93,94,95,96,97,98,99,100,102,103,104,126,127,128,129,134,135,136,137,138,139,140,147,152,],[58,-44,-39,-40,-41,-42,-43,58,-33,-34,58,58,-44,58,58,58,58,58,58,58,58,58,-31,-32,58,58,58,58,58,58,58,58,-48,-49,58,-45,-46,-47,58,58,58,58,58,58,58,58,58,]),'DOTADD':([28,30,31,32,33,34,35,49,63,64,71,74,75,77,79,81,83,85,86,89,90,91,92,93,94,95,96,97,98,99,100,102,103,104,126,127,128,129,134,135,136,137,138,139,140,147,152,],[59,-44,-39,-40,-41,-42,-43,59,-33,-34,59,59,-44,59,59,59,59,59,59,59,-29,-30,-31,-32,-35,-36,-37,-38,59,59,59,59,-48,-49,59,-45,-46,-47,59,59,59,59,59,59,59,59,59,]),'DOTSUB':([28,30,31,32,33,34,35,49,63,64,71,74,75,77,79,81,83,85,86,89,90,91,92,93,94,95,96,97,98,99,100,102,103,104,126,127,128,129,134,135,136,137,138,139,140,147,152,],[60,-44,-39,-40,-41,-42,-43,60,-33,-34,60,60,-44,60,60,60,60,60,60,60,-29,-30,-31,-32,-35,-36,-37,-38,60,60,60,60,-48,-49,60,-45,-46,-47,60,60,60,60,60,60,60,60,60,]),'DOTMUL':([28,30,31,32,33,34,35,49,63,64,71,74,75,77,79,81,83,85,86,89,90,91,92,93,94,95,96,97,98,99,100,102,103,104,126,127,128,129,134,135,136,137,138,139,140,147,152,],[61,-44,-39,-40,-41,-42,-43,61,-33,-34,61,61,-44,61,61,61,61,61,61,61,61,61,-31,-32,61,61,-37,-38,61,61,61,61,-48,-49,61,-45,-46,-47,61,61,61,61,61,61,61,61,61,]),'DOTDIVIDE':([28,30,31,32,33,34,35,49,63,64,71,74,75,77,79,81,83,85,86,89,90,91,92,93,94,95,96,97,98,99,100,102,103,104,126,127,128,129,134,135,136,137,138,139,140,147,152,],[62,-44,-39,-40,-41,-42,-43,62,-33,-34,62,62,-44,62,62,62,62,62,62,62,62,62,-31,-32,62,62,-37,-38,62,62,62,62,-48,-49,62,-45,-46,-47,62,62,62,62,62,62,62,62,62,]),"'":([30,75,],[64,64,]),']':([30,31,32,33,34,35,63,64,69,70,71,86,90,91,92,93,94,95,96,97,101,102,103,104,127,128,129,130,132,140,144,149,152,],[-44,-39,-40,-41,-42,-43,-33,-34,103,104,-51,124,-29,-30,-31,-32,-35,-36,-37,-38,130,-51,-48,-49,-45,-46,-47,-53,-50,146,-54,-52,-55,]),'GREATER':([30,31,32,33,34,35,63,64,85,90,91,92,93,94,95,96,97,103,104,127,128,129,],[-44,-39,-40,-41,-42,-43,-33,-34,117,-29,-30,-31,-32,-35,-36,-37,-38,-48,-49,-45,-46,-47,]),'LESS':([30,31,32,33,34,35,63,64,85,90,91,92,93,94,95,96,97,103,104,127,128,129,],[-44,-39,-40,-41,-42,-43,-33,-34,118,-29,-30,-31,-32,-35,-36,-37,-38,-48,-49,-45,-46,-47,]),'GREATEREQ':([30,31,32,33,34,35,63,64,85,90,91,92,93,94,95,96,97,103,104,127,128,129,],[-44,-39,-40,-41,-42,-43,-33,-34,119,-29,-30,-31,-32,-35,-36,-37,-38,-48,-49,-45,-46,-47,]),'LESSEQ':([30,31,32,33,34,35,63,64,85,90,91,92,93,94,95,96,97,103,104,127,128,129,],[-44,-39,-40,-41,-42,-43,-33,-34,120,-29,-30,-31,-32,-35,-36,-37,-38,-48,-49,-45,-46,-47,]),'NOTEQ':([30,31,32,33,34,35,63,64,85,90,91,92,93,94,95,96,97,103,104,127,128,129,],[-44,-39,-40,-41,-42,-43,-33,-34,121,-29,-30,-31,-32,-35,-36,-37,-38,-48,-49,-45,-46,-47,]),'EQ':([30,31,32,33,34,35,63,64,85,90,91,92,93,94,95,96,97,103,104,127,128,129,],[-44,-39,-40,-41,-42,-43,-33,-34,122,-29,-30,-31,-32,-35,-36,-37,-38,-48,-49,-45,-46,-47,]),')':([30,31,32,33,34,35,63,64,84,87,90,91,92,93,94,95,96,97,98,99,100,103,104,127,128,129,134,135,136,137,138,139,],[-44,-39,-40,-41,-42,-43,-33,-34,116,125,-29,-30,-31,-32,-35,-36,-37,-38,127,128,129,-48,-49,-45,-46,-47,-56,-57,-58,-59,-60,-61,]),':':([30,31,32,33,34,35,63,64,90,91,92,93,94,95,96,97,103,104,126,127,128,129,],[-44,-39,-40,-41,-42,-43,-33,-34,-29,-30,-31,-32,-35,-36,-37,-38,-48,-49,142,-45,-46,-47,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'instructions_opt':([0,],[2,]),'instructions':([0,12,],[3,40,]),'instruction':([0,3,12,40,116,125,145,147,],[4,23,4,23,133,141,150,151,]),'assignment':([0,3,12,40,116,125,145,147,],[5,5,5,5,5,5,5,5,]),'if_stmt':([0,3,12,40,116,125,145,147,],[6,6,6,6,6,6,6,6,]),'loops':([0,3,12,40,116,125,145,147,],[7,7,7,7,7,7,7,7,]),'break':([0,3,12,40,116,125,145,147,],[8,8,8,8,8,8,8,8,]),'continue':([0,3,12,40,116,125,145,147,],[9,9,9,9,9,9,9,9,]),'return_expr':([0,3,12,40,116,125,145,147,],[10,10,10,10,10,10,10,10,]),'id_change':([0,3,12,40,41,42,43,44,45,116,125,145,147,],[13,13,13,13,73,76,78,80,82,13,13,13,13,]),'while_l':([0,3,12,40,116,125,145,147,],[15,15,15,15,15,15,15,15,]),'for_l':([0,3,12,40,116,125,145,147,],[16,16,16,16,16,16,16,16,]),'create_stmt':([11,],[25,]),'p_print_list':([11,],[26,]),'expression':([11,19,29,39,41,42,43,44,45,46,50,51,54,55,56,57,58,59,60,61,62,65,66,67,68,88,105,117,118,119,120,121,122,123,131,142,148,153,],[28,49,63,71,74,77,79,81,83,85,86,85,89,90,91,92,93,94,95,96,97,98,99,100,102,126,71,134,135,136,137,138,139,140,102,147,152,152,]),'matrix_expression':([11,19,29,39,41,42,43,44,45,46,50,51,54,55,56,57,58,59,60,61,62,65,66,67,68,88,105,117,118,119,120,121,122,123,131,142,148,153,],[31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,]),'matrix_create':([11,19,29,39,41,42,43,44,45,46,50,51,54,55,56,57,58,59,60,61,62,65,66,67,68,88,105,117,118,119,120,121,122,123,131,142,148,153,],[32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,]),'vector_create':([11,19,29,39,41,42,43,44,45,46,50,51,54,55,56,57,58,59,60,61,62,65,66,67,68,88,105,117,118,119,120,121,122,123,131,142,148,153,],[33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,]),'matrix_rows':([39,68,143,],[69,69,149,]),'vector_elems':([39,68,105,131,],[70,70,132,132,]),'condition':([46,51,],[84,87,]),'matrix_elems':([68,131,148,153,],[101,144,101,144,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> instructions_opt','program',1,'p_program','Mparser.py',23),
  ('instructions_opt -> instructions','instructions_opt',1,'p_instructions_opt_1','Mparser.py',27),
  ('instructions_opt -> <empty>','instructions_opt',0,'p_instructions_opt_2','Mparser.py',31),
  ('instructions -> instructions instruction','instructions',2,'p_instructions_1','Mparser.py',35),
  ('instructions -> instruction','instructions',1,'p_instructions_2','Mparser.py',39),
  ('instruction -> assignment','instruction',1,'p_instruction','Mparser.py',43),
  ('instruction -> if_stmt','instruction',1,'p_instruction','Mparser.py',44),
  ('instruction -> loops','instruction',1,'p_instruction','Mparser.py',45),
  ('instruction -> break','instruction',1,'p_instruction','Mparser.py',46),
  ('instruction -> continue','instruction',1,'p_instruction','Mparser.py',47),
  ('instruction -> return_expr ;','instruction',2,'p_instruction','Mparser.py',48),
  ('instruction -> PRINT create_stmt ;','instruction',3,'p_instruction_2','Mparser.py',52),
  ('instruction -> { instructions }','instruction',3,'p_instruction_brackets','Mparser.py',56),
  ('continue -> CONTINUE ;','continue',2,'p_continue','Mparser.py',60),
  ('break -> BREAK ;','break',2,'p_break','Mparser.py',64),
  ('id_change -> ID','id_change',1,'p_id_change','Mparser.py',68),
  ('id_change -> ID [ expression , expression ]','id_change',6,'p_id_change','Mparser.py',69),
  ('id_change -> ID [ expression ]','id_change',4,'p_id_change','Mparser.py',70),
  ('assignment -> id_change = expression ;','assignment',4,'p_assignment','Mparser.py',79),
  ('assignment -> id_change ADDASSIGN expression ;','assignment',4,'p_assignment','Mparser.py',80),
  ('assignment -> id_change SUBASSIGN expression ;','assignment',4,'p_assignment','Mparser.py',81),
  ('assignment -> id_change MULASSIGN expression ;','assignment',4,'p_assignment','Mparser.py',82),
  ('assignment -> id_change DIVASSIGN expression ;','assignment',4,'p_assignment','Mparser.py',83),
  ('assignment -> id_change = id_change ;','assignment',4,'p_assignment','Mparser.py',84),
  ('assignment -> id_change ADDASSIGN id_change ;','assignment',4,'p_assignment','Mparser.py',85),
  ('assignment -> id_change SUBASSIGN id_change ;','assignment',4,'p_assignment','Mparser.py',86),
  ('assignment -> id_change MULASSIGN id_change ;','assignment',4,'p_assignment','Mparser.py',87),
  ('assignment -> id_change DIVASSIGN id_change ;','assignment',4,'p_assignment','Mparser.py',88),
  ('expression -> expression ADD expression','expression',3,'p_expression_binop','Mparser.py',92),
  ('expression -> expression MINUS expression','expression',3,'p_expression_binop','Mparser.py',93),
  ('expression -> expression MUL expression','expression',3,'p_expression_binop','Mparser.py',94),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression_binop','Mparser.py',95),
  ('expression -> MINUS expression','expression',2,'p_expressions_unaryneg','Mparser.py',99),
  ("expression -> ID '",'expression',2,'p_expressions_transpose','Mparser.py',103),
  ('expression -> expression DOTADD expression','expression',3,'p_expression_matrixop','Mparser.py',107),
  ('expression -> expression DOTSUB expression','expression',3,'p_expression_matrixop','Mparser.py',108),
  ('expression -> expression DOTMUL expression','expression',3,'p_expression_matrixop','Mparser.py',109),
  ('expression -> expression DOTDIVIDE expression','expression',3,'p_expression_matrixop','Mparser.py',110),
  ('expression -> matrix_expression','expression',1,'p_expression_number','Mparser.py',114),
  ('expression -> matrix_create','expression',1,'p_expression_number','Mparser.py',115),
  ('expression -> vector_create','expression',1,'p_expression_number','Mparser.py',116),
  ('expression -> INTNUM','expression',1,'p_intnum','Mparser.py',120),
  ('expression -> FLOAT','expression',1,'p_float','Mparser.py',124),
  ('expression -> ID','expression',1,'p_expression_id','Mparser.py',128),
  ('matrix_expression -> ZEROS ( expression )','matrix_expression',4,'p_matrix_expression_z','Mparser.py',132),
  ('matrix_expression -> ONES ( expression )','matrix_expression',4,'p_matrix_expression_o','Mparser.py',136),
  ('matrix_expression -> EYE ( expression )','matrix_expression',4,'p_matrix_expression_e','Mparser.py',140),
  ('matrix_create -> [ matrix_rows ]','matrix_create',3,'p_matrix_create','Mparser.py',144),
  ('vector_create -> [ vector_elems ]','vector_create',3,'p_vector_create','Mparser.py',148),
  ('vector_elems -> expression , vector_elems','vector_elems',3,'p_vector_elems','Mparser.py',152),
  ('vector_elems -> expression','vector_elems',1,'p_vector_elems','Mparser.py',153),
  ('matrix_rows -> [ matrix_elems ] , matrix_rows','matrix_rows',5,'p_matrix_rows','Mparser.py',160),
  ('matrix_rows -> [ matrix_elems ]','matrix_rows',3,'p_matrix_rows','Mparser.py',161),
  ('matrix_elems -> expression , matrix_elems','matrix_elems',3,'p_matrix_elems','Mparser.py',168),
  ('matrix_elems -> expression','matrix_elems',1,'p_matrix_elems','Mparser.py',169),
  ('condition -> expression GREATER expression','condition',3,'p_condition','Mparser.py',176),
  ('condition -> expression LESS expression','condition',3,'p_condition','Mparser.py',177),
  ('condition -> expression GREATEREQ expression','condition',3,'p_condition','Mparser.py',178),
  ('condition -> expression LESSEQ expression','condition',3,'p_condition','Mparser.py',179),
  ('condition -> expression NOTEQ expression','condition',3,'p_condition','Mparser.py',180),
  ('condition -> expression EQ expression','condition',3,'p_condition','Mparser.py',181),
  ('if_stmt -> IF ( condition ) instruction','if_stmt',5,'p_if_stmt','Mparser.py',185),
  ('if_stmt -> IF ( condition ) instruction ELSE instruction','if_stmt',7,'p_if_stmt','Mparser.py',186),
  ('create_stmt -> p_print_list','create_stmt',1,'p_create_stmt','Mparser.py',194),
  ('p_print_list -> STRING','p_print_list',1,'p_print_list_1','Mparser.py',198),
  ('p_print_list -> p_print_list , expression','p_print_list',3,'p_print_list_2','Mparser.py',202),
  ('p_print_list -> expression','p_print_list',1,'p_print_list_2','Mparser.py',203),
  ('loops -> while_l','loops',1,'p_loops','Mparser.py',211),
  ('loops -> for_l','loops',1,'p_loops','Mparser.py',212),
  ('while_l -> WHILE ( condition ) instruction','while_l',5,'p_while_l','Mparser.py',216),
  ('for_l -> FOR ID = expression : expression instruction','for_l',7,'p_for_l','Mparser.py',220),
  ('return_expr -> RETURN','return_expr',1,'p_return_expr','Mparser.py',224),
  ('return_expr -> RETURN expression','return_expr',2,'p_return_expr','Mparser.py',225),
]
