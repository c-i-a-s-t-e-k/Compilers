
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'nonassocIFXnonassocELSEleftDOTADDDOTSUBleftADDMINUSleftDOTMULDOTDIVIDEleftDIVIDEMULrightUMINUSADD ADDASSIGN BREAK CONTINUE DIVASSIGN DIVIDE DOTADD DOTDIVIDE DOTMUL DOTSUB ELSE EQ EYE FLOAT FOR GREATER GREATEREQ ID IF INTNUM LESS LESSEQ MINUS MUL MULASSIGN NOTEQ ONES PRINT RETURN STRING SUBASSIGN WHILE ZEROSprogram : instructions_optinstructions_opt : instructions instructions_opt : instructions : instructions instruction instructions : instruction instruction : assignment \';\'\n                    | if_stmt\n                    | loops\n                    | BREAK \';\'\n                    | CONTINUE \';\'\n                    | return_expr \';\'instruction : PRINT create_stmt \';\'instruction : \'{\' instructions \'}\'id_change : ID \n                    | ID \'[\' expression \',\' expression \']\'assignment : id_change \'=\' expression\n                    | id_change ADDASSIGN expression\n                    | id_change SUBASSIGN expression\n                    | id_change MULASSIGN expression\n                    | id_change DIVASSIGN expressionexpression : expression ADD expression\n                    | expression MINUS expression\n                    | expression MUL expression\n                    | expression DIVIDE expressionexpression : MINUS expression %prec UMINUSexpression : ID "\'"expression : expression DOTADD expression\n                    | expression DOTSUB expression\n                    | expression DOTMUL expression\n                    | expression DOTDIVIDE expressionexpression : matrix_expression\n                    | matrix_createexpression : INTNUMexpression : FLOATexpression : IDmatrix_expression : ZEROS \'(\' expression \')\' matrix_expression : ONES \'(\' expression \')\' matrix_expression : EYE \'(\' expression \')\' matrix_create : \'[\' matrix_rows \']\'matrix_rows : \'[\' matrix_elems \']\' \',\' matrix_rows\n                    | \'[\' matrix_elems \']\'matrix_elems : expression \',\' matrix_elems\n                    | expressioncondition : expression GREATER expression\n                    | expression LESS expression\n                    | expression GREATEREQ expression\n                    | expression LESSEQ expression\n                    | expression NOTEQ expression\n                    | expression EQ expressionif_stmt : IF \'(\' condition \')\' instruction %prec IFX\n                | IF \'(\' condition \')\' instruction ELSE instruction\n                create_stmt : p_print_listp_print_list : STRING p_print_list : p_print_list \',\' expression\n                    | expressionloops : while_l\n                | for_lwhile_l : WHILE "(" condition ")" instructionfor_l : FOR ID "=" expression ":" expression instructionreturn_expr : RETURN\n                    | RETURN expression'
    
_lr_action_items = {'$end':([0,1,2,3,4,6,7,15,16,21,22,23,24,25,51,68,109,117,125,126,],[-3,0,-1,-2,-5,-7,-8,-56,-57,-4,-6,-9,-10,-11,-12,-13,-50,-58,-51,-59,]),'BREAK':([0,3,4,6,7,12,15,16,21,22,23,24,25,31,32,33,34,35,40,51,61,62,68,80,81,82,83,84,85,86,87,93,94,102,104,105,106,109,117,121,123,125,126,],[8,8,-5,-7,-8,8,-56,-57,-4,-6,-9,-10,-11,-35,-31,-32,-33,-34,8,-12,-25,-26,-13,-21,-22,-23,-24,-27,-28,-29,-30,-39,8,8,-36,-37,-38,-50,-58,8,8,-51,-59,]),'CONTINUE':([0,3,4,6,7,12,15,16,21,22,23,24,25,31,32,33,34,35,40,51,61,62,68,80,81,82,83,84,85,86,87,93,94,102,104,105,106,109,117,121,123,125,126,],[9,9,-5,-7,-8,9,-56,-57,-4,-6,-9,-10,-11,-35,-31,-32,-33,-34,9,-12,-25,-26,-13,-21,-22,-23,-24,-27,-28,-29,-30,-39,9,9,-36,-37,-38,-50,-58,9,9,-51,-59,]),'PRINT':([0,3,4,6,7,12,15,16,21,22,23,24,25,31,32,33,34,35,40,51,61,62,68,80,81,82,83,84,85,86,87,93,94,102,104,105,106,109,117,121,123,125,126,],[11,11,-5,-7,-8,11,-56,-57,-4,-6,-9,-10,-11,-35,-31,-32,-33,-34,11,-12,-25,-26,-13,-21,-22,-23,-24,-27,-28,-29,-30,-39,11,11,-36,-37,-38,-50,-58,11,11,-51,-59,]),'{':([0,3,4,6,7,12,15,16,21,22,23,24,25,31,32,33,34,35,40,51,61,62,68,80,81,82,83,84,85,86,87,93,94,102,104,105,106,109,117,121,123,125,126,],[12,12,-5,-7,-8,12,-56,-57,-4,-6,-9,-10,-11,-35,-31,-32,-33,-34,12,-12,-25,-26,-13,-21,-22,-23,-24,-27,-28,-29,-30,-39,12,12,-36,-37,-38,-50,-58,12,12,-51,-59,]),'IF':([0,3,4,6,7,12,15,16,21,22,23,24,25,31,32,33,34,35,40,51,61,62,68,80,81,82,83,84,85,86,87,93,94,102,104,105,106,109,117,121,123,125,126,],[14,14,-5,-7,-8,14,-56,-57,-4,-6,-9,-10,-11,-35,-31,-32,-33,-34,14,-12,-25,-26,-13,-21,-22,-23,-24,-27,-28,-29,-30,-39,14,14,-36,-37,-38,-50,-58,14,14,-51,-59,]),'RETURN':([0,3,4,6,7,12,15,16,21,22,23,24,25,31,32,33,34,35,40,51,61,62,68,80,81,82,83,84,85,86,87,93,94,102,104,105,106,109,117,121,123,125,126,],[17,17,-5,-7,-8,17,-56,-57,-4,-6,-9,-10,-11,-35,-31,-32,-33,-34,17,-12,-25,-26,-13,-21,-22,-23,-24,-27,-28,-29,-30,-39,17,17,-36,-37,-38,-50,-58,17,17,-51,-59,]),'ID':([0,3,4,6,7,11,12,15,16,17,20,21,22,23,24,25,30,31,32,33,34,35,40,41,42,43,44,45,46,48,49,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,68,78,80,81,82,83,84,85,86,87,93,94,95,96,97,98,99,100,101,102,104,105,106,108,109,117,118,121,123,125,126,],[18,18,-5,-7,-8,31,18,-56,-57,31,50,-4,-6,-9,-10,-11,31,-35,-31,-32,-33,-34,18,31,31,31,31,31,31,31,31,-12,31,31,31,31,31,31,31,31,31,-25,-26,31,31,31,31,-13,31,-21,-22,-23,-24,-27,-28,-29,-30,-39,18,31,31,31,31,31,31,31,18,-36,-37,-38,31,-50,-58,31,18,18,-51,-59,]),'WHILE':([0,3,4,6,7,12,15,16,21,22,23,24,25,31,32,33,34,35,40,51,61,62,68,80,81,82,83,84,85,86,87,93,94,102,104,105,106,109,117,121,123,125,126,],[19,19,-5,-7,-8,19,-56,-57,-4,-6,-9,-10,-11,-35,-31,-32,-33,-34,19,-12,-25,-26,-13,-21,-22,-23,-24,-27,-28,-29,-30,-39,19,19,-36,-37,-38,-50,-58,19,19,-51,-59,]),'FOR':([0,3,4,6,7,12,15,16,21,22,23,24,25,31,32,33,34,35,40,51,61,62,68,80,81,82,83,84,85,86,87,93,94,102,104,105,106,109,117,121,123,125,126,],[20,20,-5,-7,-8,20,-56,-57,-4,-6,-9,-10,-11,-35,-31,-32,-33,-34,20,-12,-25,-26,-13,-21,-22,-23,-24,-27,-28,-29,-30,-39,20,20,-36,-37,-38,-50,-58,20,20,-51,-59,]),'}':([4,6,7,15,16,21,22,23,24,25,40,51,68,109,117,125,126,],[-5,-7,-8,-56,-57,-4,-6,-9,-10,-11,68,-12,-13,-50,-58,-51,-59,]),';':([5,8,9,10,17,26,27,28,29,31,32,33,34,35,47,61,62,69,70,71,72,73,79,80,81,82,83,84,85,86,87,93,104,105,106,],[22,23,24,25,-60,51,-52,-53,-55,-35,-31,-32,-33,-34,-61,-25,-26,-16,-17,-18,-19,-20,-54,-21,-22,-23,-24,-27,-28,-29,-30,-39,-36,-37,-38,]),'ELSE':([6,7,15,16,22,23,24,25,51,68,109,117,125,126,],[-7,-8,-56,-57,-6,-9,-10,-11,-12,-13,121,-58,-51,-59,]),'STRING':([11,],[28,]),'MINUS':([11,17,29,30,31,32,33,34,35,41,42,43,44,45,46,47,48,49,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,69,70,71,72,73,75,76,78,79,80,81,82,83,84,85,86,87,88,89,90,92,93,95,96,97,98,99,100,101,103,104,105,106,108,110,111,112,113,114,115,116,118,123,],[30,30,54,30,-35,-31,-32,-33,-34,30,30,30,30,30,30,54,30,30,30,30,30,30,30,30,30,30,30,-25,-26,30,30,30,30,54,54,54,54,54,54,54,30,54,-21,-22,-23,-24,54,54,-29,-30,54,54,54,54,-39,30,30,30,30,30,30,30,54,-36,-37,-38,30,54,54,54,54,54,54,54,30,54,]),'INTNUM':([11,17,30,41,42,43,44,45,46,48,49,52,53,54,55,56,57,58,59,60,63,64,65,66,78,95,96,97,98,99,100,101,108,118,],[34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,]),'FLOAT':([11,17,30,41,42,43,44,45,46,48,49,52,53,54,55,56,57,58,59,60,63,64,65,66,78,95,96,97,98,99,100,101,108,118,],[35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,]),'ZEROS':([11,17,30,41,42,43,44,45,46,48,49,52,53,54,55,56,57,58,59,60,63,64,65,66,78,95,96,97,98,99,100,101,108,118,],[36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,]),'ONES':([11,17,30,41,42,43,44,45,46,48,49,52,53,54,55,56,57,58,59,60,63,64,65,66,78,95,96,97,98,99,100,101,108,118,],[37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,]),'EYE':([11,17,30,41,42,43,44,45,46,48,49,52,53,54,55,56,57,58,59,60,63,64,65,66,78,95,96,97,98,99,100,101,108,118,],[38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,]),'[':([11,17,18,30,39,41,42,43,44,45,46,48,49,52,53,54,55,56,57,58,59,60,63,64,65,66,78,95,96,97,98,99,100,101,108,118,119,],[39,39,48,39,66,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,66,]),'=':([13,18,50,122,],[41,-14,78,-15,]),'ADDASSIGN':([13,18,122,],[42,-14,-15,]),'SUBASSIGN':([13,18,122,],[43,-14,-15,]),'MULASSIGN':([13,18,122,],[44,-14,-15,]),'DIVASSIGN':([13,18,122,],[45,-14,-15,]),'(':([14,19,36,37,38,],[46,49,63,64,65,]),',':([27,28,29,31,32,33,34,35,61,62,76,79,80,81,82,83,84,85,86,87,92,93,104,105,106,107,],[52,-53,-55,-35,-31,-32,-33,-34,-25,-26,101,-54,-21,-22,-23,-24,-27,-28,-29,-30,108,-39,-36,-37,-38,119,]),'ADD':([29,31,32,33,34,35,47,61,62,69,70,71,72,73,75,76,79,80,81,82,83,84,85,86,87,88,89,90,92,93,103,104,105,106,110,111,112,113,114,115,116,123,],[53,-35,-31,-32,-33,-34,53,-25,-26,53,53,53,53,53,53,53,53,-21,-22,-23,-24,53,53,-29,-30,53,53,53,53,-39,53,-36,-37,-38,53,53,53,53,53,53,53,53,]),'MUL':([29,31,32,33,34,35,47,61,62,69,70,71,72,73,75,76,79,80,81,82,83,84,85,86,87,88,89,90,92,93,103,104,105,106,110,111,112,113,114,115,116,123,],[55,-35,-31,-32,-33,-34,55,-25,-26,55,55,55,55,55,55,55,55,55,55,-23,-24,55,55,55,55,55,55,55,55,-39,55,-36,-37,-38,55,55,55,55,55,55,55,55,]),'DIVIDE':([29,31,32,33,34,35,47,61,62,69,70,71,72,73,75,76,79,80,81,82,83,84,85,86,87,88,89,90,92,93,103,104,105,106,110,111,112,113,114,115,116,123,],[56,-35,-31,-32,-33,-34,56,-25,-26,56,56,56,56,56,56,56,56,56,56,-23,-24,56,56,56,56,56,56,56,56,-39,56,-36,-37,-38,56,56,56,56,56,56,56,56,]),'DOTADD':([29,31,32,33,34,35,47,61,62,69,70,71,72,73,75,76,79,80,81,82,83,84,85,86,87,88,89,90,92,93,103,104,105,106,110,111,112,113,114,115,116,123,],[57,-35,-31,-32,-33,-34,57,-25,-26,57,57,57,57,57,57,57,57,-21,-22,-23,-24,-27,-28,-29,-30,57,57,57,57,-39,57,-36,-37,-38,57,57,57,57,57,57,57,57,]),'DOTSUB':([29,31,32,33,34,35,47,61,62,69,70,71,72,73,75,76,79,80,81,82,83,84,85,86,87,88,89,90,92,93,103,104,105,106,110,111,112,113,114,115,116,123,],[58,-35,-31,-32,-33,-34,58,-25,-26,58,58,58,58,58,58,58,58,-21,-22,-23,-24,-27,-28,-29,-30,58,58,58,58,-39,58,-36,-37,-38,58,58,58,58,58,58,58,58,]),'DOTMUL':([29,31,32,33,34,35,47,61,62,69,70,71,72,73,75,76,79,80,81,82,83,84,85,86,87,88,89,90,92,93,103,104,105,106,110,111,112,113,114,115,116,123,],[59,-35,-31,-32,-33,-34,59,-25,-26,59,59,59,59,59,59,59,59,59,59,-23,-24,59,59,-29,-30,59,59,59,59,-39,59,-36,-37,-38,59,59,59,59,59,59,59,59,]),'DOTDIVIDE':([29,31,32,33,34,35,47,61,62,69,70,71,72,73,75,76,79,80,81,82,83,84,85,86,87,88,89,90,92,93,103,104,105,106,110,111,112,113,114,115,116,123,],[60,-35,-31,-32,-33,-34,60,-25,-26,60,60,60,60,60,60,60,60,60,60,-23,-24,60,60,-29,-30,60,60,60,60,-39,60,-36,-37,-38,60,60,60,60,60,60,60,60,]),"'":([31,],[62,]),'GREATER':([31,32,33,34,35,61,62,75,80,81,82,83,84,85,86,87,93,104,105,106,],[-35,-31,-32,-33,-34,-25,-26,95,-21,-22,-23,-24,-27,-28,-29,-30,-39,-36,-37,-38,]),'LESS':([31,32,33,34,35,61,62,75,80,81,82,83,84,85,86,87,93,104,105,106,],[-35,-31,-32,-33,-34,-25,-26,96,-21,-22,-23,-24,-27,-28,-29,-30,-39,-36,-37,-38,]),'GREATEREQ':([31,32,33,34,35,61,62,75,80,81,82,83,84,85,86,87,93,104,105,106,],[-35,-31,-32,-33,-34,-25,-26,97,-21,-22,-23,-24,-27,-28,-29,-30,-39,-36,-37,-38,]),'LESSEQ':([31,32,33,34,35,61,62,75,80,81,82,83,84,85,86,87,93,104,105,106,],[-35,-31,-32,-33,-34,-25,-26,98,-21,-22,-23,-24,-27,-28,-29,-30,-39,-36,-37,-38,]),'NOTEQ':([31,32,33,34,35,61,62,75,80,81,82,83,84,85,86,87,93,104,105,106,],[-35,-31,-32,-33,-34,-25,-26,99,-21,-22,-23,-24,-27,-28,-29,-30,-39,-36,-37,-38,]),'EQ':([31,32,33,34,35,61,62,75,80,81,82,83,84,85,86,87,93,104,105,106,],[-35,-31,-32,-33,-34,-25,-26,100,-21,-22,-23,-24,-27,-28,-29,-30,-39,-36,-37,-38,]),')':([31,32,33,34,35,61,62,74,77,80,81,82,83,84,85,86,87,88,89,90,93,104,105,106,110,111,112,113,114,115,],[-35,-31,-32,-33,-34,-25,-26,94,102,-21,-22,-23,-24,-27,-28,-29,-30,104,105,106,-39,-36,-37,-38,-44,-45,-46,-47,-48,-49,]),']':([31,32,33,34,35,61,62,67,80,81,82,83,84,85,86,87,91,92,93,104,105,106,107,116,120,124,],[-35,-31,-32,-33,-34,-25,-26,93,-21,-22,-23,-24,-27,-28,-29,-30,107,-43,-39,-36,-37,-38,-41,122,-42,-40,]),':':([31,32,33,34,35,61,62,80,81,82,83,84,85,86,87,93,103,104,105,106,],[-35,-31,-32,-33,-34,-25,-26,-21,-22,-23,-24,-27,-28,-29,-30,-39,118,-36,-37,-38,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'instructions_opt':([0,],[2,]),'instructions':([0,12,],[3,40,]),'instruction':([0,3,12,40,94,102,121,123,],[4,21,4,21,109,117,125,126,]),'assignment':([0,3,12,40,94,102,121,123,],[5,5,5,5,5,5,5,5,]),'if_stmt':([0,3,12,40,94,102,121,123,],[6,6,6,6,6,6,6,6,]),'loops':([0,3,12,40,94,102,121,123,],[7,7,7,7,7,7,7,7,]),'return_expr':([0,3,12,40,94,102,121,123,],[10,10,10,10,10,10,10,10,]),'id_change':([0,3,12,40,94,102,121,123,],[13,13,13,13,13,13,13,13,]),'while_l':([0,3,12,40,94,102,121,123,],[15,15,15,15,15,15,15,15,]),'for_l':([0,3,12,40,94,102,121,123,],[16,16,16,16,16,16,16,16,]),'create_stmt':([11,],[26,]),'p_print_list':([11,],[27,]),'expression':([11,17,30,41,42,43,44,45,46,48,49,52,53,54,55,56,57,58,59,60,63,64,65,66,78,95,96,97,98,99,100,101,108,118,],[29,47,61,69,70,71,72,73,75,76,75,79,80,81,82,83,84,85,86,87,88,89,90,92,103,110,111,112,113,114,115,116,92,123,]),'matrix_expression':([11,17,30,41,42,43,44,45,46,48,49,52,53,54,55,56,57,58,59,60,63,64,65,66,78,95,96,97,98,99,100,101,108,118,],[32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,]),'matrix_create':([11,17,30,41,42,43,44,45,46,48,49,52,53,54,55,56,57,58,59,60,63,64,65,66,78,95,96,97,98,99,100,101,108,118,],[33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,]),'matrix_rows':([39,119,],[67,124,]),'condition':([46,49,],[74,77,]),'matrix_elems':([66,108,],[91,120,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> instructions_opt','program',1,'p_program','Mparser.py',30),
  ('instructions_opt -> instructions','instructions_opt',1,'p_instructions_opt_1','Mparser.py',34),
  ('instructions_opt -> <empty>','instructions_opt',0,'p_instructions_opt_2','Mparser.py',38),
  ('instructions -> instructions instruction','instructions',2,'p_instructions_1','Mparser.py',42),
  ('instructions -> instruction','instructions',1,'p_instructions_2','Mparser.py',46),
  ('instruction -> assignment ;','instruction',2,'p_instruction','Mparser.py',50),
  ('instruction -> if_stmt','instruction',1,'p_instruction','Mparser.py',51),
  ('instruction -> loops','instruction',1,'p_instruction','Mparser.py',52),
  ('instruction -> BREAK ;','instruction',2,'p_instruction','Mparser.py',53),
  ('instruction -> CONTINUE ;','instruction',2,'p_instruction','Mparser.py',54),
  ('instruction -> return_expr ;','instruction',2,'p_instruction','Mparser.py',55),
  ('instruction -> PRINT create_stmt ;','instruction',3,'p_instruction_2','Mparser.py',59),
  ('instruction -> { instructions }','instruction',3,'p_instruction_brackets','Mparser.py',63),
  ('id_change -> ID','id_change',1,'p_id_change','Mparser.py',68),
  ('id_change -> ID [ expression , expression ]','id_change',6,'p_id_change','Mparser.py',69),
  ('assignment -> id_change = expression','assignment',3,'p_assignment','Mparser.py',76),
  ('assignment -> id_change ADDASSIGN expression','assignment',3,'p_assignment','Mparser.py',77),
  ('assignment -> id_change SUBASSIGN expression','assignment',3,'p_assignment','Mparser.py',78),
  ('assignment -> id_change MULASSIGN expression','assignment',3,'p_assignment','Mparser.py',79),
  ('assignment -> id_change DIVASSIGN expression','assignment',3,'p_assignment','Mparser.py',80),
  ('expression -> expression ADD expression','expression',3,'p_expression_binop','Mparser.py',84),
  ('expression -> expression MINUS expression','expression',3,'p_expression_binop','Mparser.py',85),
  ('expression -> expression MUL expression','expression',3,'p_expression_binop','Mparser.py',86),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression_binop','Mparser.py',87),
  ('expression -> MINUS expression','expression',2,'p_expressions_unaryneg','Mparser.py',91),
  ("expression -> ID '",'expression',2,'p_expressions_transpose','Mparser.py',95),
  ('expression -> expression DOTADD expression','expression',3,'p_expression_matrixop','Mparser.py',99),
  ('expression -> expression DOTSUB expression','expression',3,'p_expression_matrixop','Mparser.py',100),
  ('expression -> expression DOTMUL expression','expression',3,'p_expression_matrixop','Mparser.py',101),
  ('expression -> expression DOTDIVIDE expression','expression',3,'p_expression_matrixop','Mparser.py',102),
  ('expression -> matrix_expression','expression',1,'p_expression_number','Mparser.py',106),
  ('expression -> matrix_create','expression',1,'p_expression_number','Mparser.py',107),
  ('expression -> INTNUM','expression',1,'p_intnum','Mparser.py',111),
  ('expression -> FLOAT','expression',1,'p_float','Mparser.py',115),
  ('expression -> ID','expression',1,'p_expression_id','Mparser.py',119),
  ('matrix_expression -> ZEROS ( expression )','matrix_expression',4,'p_matrix_expression_z','Mparser.py',123),
  ('matrix_expression -> ONES ( expression )','matrix_expression',4,'p_matrix_expression_o','Mparser.py',127),
  ('matrix_expression -> EYE ( expression )','matrix_expression',4,'p_matrix_expression_e','Mparser.py',131),
  ('matrix_create -> [ matrix_rows ]','matrix_create',3,'p_matrix_create','Mparser.py',135),
  ('matrix_rows -> [ matrix_elems ] , matrix_rows','matrix_rows',5,'p_matrix_rows','Mparser.py',139),
  ('matrix_rows -> [ matrix_elems ]','matrix_rows',3,'p_matrix_rows','Mparser.py',140),
  ('matrix_elems -> expression , matrix_elems','matrix_elems',3,'p_matrix_elems','Mparser.py',147),
  ('matrix_elems -> expression','matrix_elems',1,'p_matrix_elems','Mparser.py',148),
  ('condition -> expression GREATER expression','condition',3,'p_condition','Mparser.py',155),
  ('condition -> expression LESS expression','condition',3,'p_condition','Mparser.py',156),
  ('condition -> expression GREATEREQ expression','condition',3,'p_condition','Mparser.py',157),
  ('condition -> expression LESSEQ expression','condition',3,'p_condition','Mparser.py',158),
  ('condition -> expression NOTEQ expression','condition',3,'p_condition','Mparser.py',159),
  ('condition -> expression EQ expression','condition',3,'p_condition','Mparser.py',160),
  ('if_stmt -> IF ( condition ) instruction','if_stmt',5,'p_if_stmt','Mparser.py',164),
  ('if_stmt -> IF ( condition ) instruction ELSE instruction','if_stmt',7,'p_if_stmt','Mparser.py',165),
  ('create_stmt -> p_print_list','create_stmt',1,'p_create_stmt','Mparser.py',173),
  ('p_print_list -> STRING','p_print_list',1,'p_print_list_1','Mparser.py',177),
  ('p_print_list -> p_print_list , expression','p_print_list',3,'p_print_list_2','Mparser.py',181),
  ('p_print_list -> expression','p_print_list',1,'p_print_list_2','Mparser.py',182),
  ('loops -> while_l','loops',1,'p_loops','Mparser.py',190),
  ('loops -> for_l','loops',1,'p_loops','Mparser.py',191),
  ('while_l -> WHILE ( condition ) instruction','while_l',5,'p_while_l','Mparser.py',195),
  ('for_l -> FOR ID = expression : expression instruction','for_l',7,'p_for_l','Mparser.py',199),
  ('return_expr -> RETURN','return_expr',1,'p_return_expr','Mparser.py',203),
  ('return_expr -> RETURN expression','return_expr',2,'p_return_expr','Mparser.py',204),
]
