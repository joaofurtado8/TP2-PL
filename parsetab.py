
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "leftoulefteleft+-left*/cosFim Inicio atribui caracter cos e ellipsis escreva falso inteiro leia logico nao nr ou real sen string var verdadeiro axioma : Inicio code Fim code : S code : code ';' S S : E\n             | CC : escreva '(' e_list ')' ';'C : leia '(' var ')' ';' C : var atribui E ';' C : inteiro ':' code ';'C : real ':' var ';'C : logico ':' var ';'C : caracter ':' var ';' e_list : E\n                   | string  e_list : e_list ',' E\n                   | e_list ',' string N : nr N : E '+' E\n             | E '-' E\n             | E '*' E\n             | E '/' EN : cos '(' E ')'N : sen '(' E ')'B : FB : E e E\n             | E ou E F : verdadeiro  F : falso  F : nao F\n              | nao var arg_list : E\n                     | arg_list ',' E  E : var E : B\n             | N\n             | string\n             | '(' E ')'  E : var '(' arg_list ')'\n              | var '(' ')'  var_list : var\n                     | var_list ',' var  args :\n                 | var_list "
    
_lr_action_items = {'Inicio':([0,],[2,]),'$end':([1,25,],[0,-1,]),'var':([2,11,24,26,27,28,29,30,31,32,33,34,37,38,39,40,41,42,43,44,70,73,75,],[7,36,46,7,36,36,36,36,36,36,36,36,36,62,7,64,65,66,36,36,36,36,7,]),'string':([2,11,26,27,28,29,30,31,32,33,34,37,39,43,44,70,73,75,],[10,10,10,10,10,10,10,10,10,10,10,61,10,10,10,10,84,10,]),'(':([2,7,11,12,13,20,21,26,27,28,29,30,31,32,33,34,36,37,39,43,44,70,73,75,],[11,33,11,37,38,43,44,11,11,11,11,11,11,11,11,11,33,11,11,11,11,11,11,11,]),'escreva':([2,26,39,75,],[12,12,12,12,]),'leia':([2,26,39,75,],[13,13,13,13,]),'inteiro':([2,26,39,75,],[14,14,14,14,]),'real':([2,26,39,75,],[15,15,15,15,]),'logico':([2,26,39,75,],[16,16,16,16,]),'caracter':([2,26,39,75,],[17,17,17,17,]),'nr':([2,11,26,27,28,29,30,31,32,33,34,37,39,43,44,70,73,75,],[19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,]),'cos':([2,11,26,27,28,29,30,31,32,33,34,37,39,43,44,70,73,75,],[20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,]),'sen':([2,11,26,27,28,29,30,31,32,33,34,37,39,43,44,70,73,75,],[21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,]),'verdadeiro':([2,11,24,26,27,28,29,30,31,32,33,34,37,39,43,44,70,73,75,],[22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,]),'falso':([2,11,24,26,27,28,29,30,31,32,33,34,37,39,43,44,70,73,75,],[23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,]),'nao':([2,11,24,26,27,28,29,30,31,32,33,34,37,39,43,44,70,73,75,],[24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,]),'Fim':([3,4,5,6,7,8,9,10,18,19,22,23,36,45,46,47,48,49,50,51,52,53,55,58,69,71,75,76,77,78,79,80,82,85,],[25,-2,-4,-5,-33,-34,-35,-36,-24,-17,-27,-28,-33,-29,-30,-3,-25,-26,-18,-19,-20,-21,-39,-37,-38,-8,-9,-10,-11,-12,-22,-23,-6,-7,]),';':([3,4,5,6,7,8,9,10,18,19,22,23,36,45,46,47,48,49,50,51,52,53,55,57,58,63,64,65,66,69,71,72,74,75,76,77,78,79,80,82,85,],[26,-2,-4,-5,-33,-34,-35,-36,-24,-17,-27,-28,-33,-29,-30,-3,-25,-26,-18,-19,-20,-21,-39,71,-37,75,76,77,78,-38,-8,82,85,-9,-10,-11,-12,-22,-23,-6,-7,]),'e':([5,7,8,9,10,18,19,22,23,35,36,45,46,48,49,50,51,52,53,55,56,57,58,60,61,67,68,69,79,80,81,83,84,],[27,-33,-34,-35,-36,-24,-17,-27,-28,27,-33,-29,-30,-25,27,-18,-19,-20,-21,-39,27,27,-37,27,-36,27,27,-38,-22,-23,27,27,-36,]),'ou':([5,7,8,9,10,18,19,22,23,35,36,45,46,48,49,50,51,52,53,55,56,57,58,60,61,67,68,69,79,80,81,83,84,],[28,-33,-34,-35,-36,-24,-17,-27,-28,28,-33,-29,-30,-25,-26,-18,-19,-20,-21,-39,28,28,-37,28,-36,28,28,-38,-22,-23,28,28,-36,]),'+':([5,7,8,9,10,18,19,22,23,35,36,45,46,48,49,50,51,52,53,55,56,57,58,60,61,67,68,69,79,80,81,83,84,],[29,-33,-34,-35,-36,-24,-17,-27,-28,29,-33,-29,-30,29,29,-18,-19,-20,-21,-39,29,29,-37,29,-36,29,29,-38,-22,-23,29,29,-36,]),'-':([5,7,8,9,10,18,19,22,23,35,36,45,46,48,49,50,51,52,53,55,56,57,58,60,61,67,68,69,79,80,81,83,84,],[30,-33,-34,-35,-36,-24,-17,-27,-28,30,-33,-29,-30,30,30,-18,-19,-20,-21,-39,30,30,-37,30,-36,30,30,-38,-22,-23,30,30,-36,]),'*':([5,7,8,9,10,18,19,22,23,35,36,45,46,48,49,50,51,52,53,55,56,57,58,60,61,67,68,69,79,80,81,83,84,],[31,-33,-34,-35,-36,-24,-17,-27,-28,31,-33,-29,-30,31,31,31,31,-20,-21,-39,31,31,-37,31,-36,31,31,-38,-22,-23,31,31,-36,]),'/':([5,7,8,9,10,18,19,22,23,35,36,45,46,48,49,50,51,52,53,55,56,57,58,60,61,67,68,69,79,80,81,83,84,],[32,-33,-34,-35,-36,-24,-17,-27,-28,32,-33,-29,-30,32,32,32,32,-20,-21,-39,32,32,-37,32,-36,32,32,-38,-22,-23,32,32,-36,]),'atribui':([7,],[34,]),')':([8,9,10,18,19,22,23,33,35,36,45,46,48,49,50,51,52,53,54,55,56,58,59,60,61,62,67,68,69,79,80,81,83,84,],[-34,-35,-36,-24,-17,-27,-28,55,58,-33,-29,-30,-25,-26,-18,-19,-20,-21,69,-39,-31,-37,72,-13,-14,74,79,80,-38,-22,-23,-32,-15,-16,]),',':([8,9,10,18,19,22,23,36,45,46,48,49,50,51,52,53,54,55,56,58,59,60,61,69,79,80,81,83,84,],[-34,-35,-36,-24,-17,-27,-28,-33,-29,-30,-25,-26,-18,-19,-20,-21,70,-39,-31,-37,73,-13,-14,-38,-22,-23,-32,-15,-16,]),':':([14,15,16,17,],[39,40,41,42,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'axioma':([0,],[1,]),'code':([2,39,],[3,63,]),'S':([2,26,39,75,],[4,47,4,47,]),'E':([2,11,26,27,28,29,30,31,32,33,34,37,39,43,44,70,73,75,],[5,35,5,48,49,50,51,52,53,56,57,60,5,67,68,81,83,5,]),'C':([2,26,39,75,],[6,6,6,6,]),'B':([2,11,26,27,28,29,30,31,32,33,34,37,39,43,44,70,73,75,],[8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,]),'N':([2,11,26,27,28,29,30,31,32,33,34,37,39,43,44,70,73,75,],[9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,]),'F':([2,11,24,26,27,28,29,30,31,32,33,34,37,39,43,44,70,73,75,],[18,18,45,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,]),'arg_list':([33,],[54,]),'e_list':([37,],[59,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> axioma","S'",1,None,None,None),
  ('axioma -> Inicio code Fim','axioma',3,'p_axioma0','logic_grammar.py',26),
  ('code -> S','code',1,'p_code0','logic_grammar.py',30),
  ('code -> code ; S','code',3,'p_code1','logic_grammar.py',34),
  ('S -> E','S',1,'p_s0','logic_grammar.py',39),
  ('S -> C','S',1,'p_s0','logic_grammar.py',40),
  ('C -> escreva ( e_list ) ;','C',5,'p_c0','logic_grammar.py',44),
  ('C -> leia ( var ) ;','C',5,'p_c1','logic_grammar.py',48),
  ('C -> var atribui E ;','C',4,'p_c2','logic_grammar.py',52),
  ('C -> inteiro : code ;','C',4,'p_c4','logic_grammar.py',59),
  ('C -> real : var ;','C',4,'p_c5','logic_grammar.py',63),
  ('C -> logico : var ;','C',4,'p_c6','logic_grammar.py',67),
  ('C -> caracter : var ;','C',4,'p_c7','logic_grammar.py',71),
  ('e_list -> E','e_list',1,'p_elist0','logic_grammar.py',75),
  ('e_list -> string','e_list',1,'p_elist0','logic_grammar.py',76),
  ('e_list -> e_list , E','e_list',3,'p_elist','logic_grammar.py',80),
  ('e_list -> e_list , string','e_list',3,'p_elist','logic_grammar.py',81),
  ('N -> nr','N',1,'p_n1','logic_grammar.py',86),
  ('N -> E + E','N',3,'p_n2','logic_grammar.py',90),
  ('N -> E - E','N',3,'p_n2','logic_grammar.py',91),
  ('N -> E * E','N',3,'p_n2','logic_grammar.py',92),
  ('N -> E / E','N',3,'p_n2','logic_grammar.py',93),
  ('N -> cos ( E )','N',4,'p_n3','logic_grammar.py',97),
  ('N -> sen ( E )','N',4,'p_n4','logic_grammar.py',101),
  ('B -> F','B',1,'p_b0','logic_grammar.py',105),
  ('B -> E e E','B',3,'p_b1','logic_grammar.py',109),
  ('B -> E ou E','B',3,'p_b1','logic_grammar.py',110),
  ('F -> verdadeiro','F',1,'p_f1','logic_grammar.py',114),
  ('F -> falso','F',1,'p_f2','logic_grammar.py',118),
  ('F -> nao F','F',2,'p_f3','logic_grammar.py',122),
  ('F -> nao var','F',2,'p_f3','logic_grammar.py',123),
  ('arg_list -> E','arg_list',1,'p_arg_list','logic_grammar.py',144),
  ('arg_list -> arg_list , E','arg_list',3,'p_arg_list','logic_grammar.py',145),
  ('E -> var','E',1,'p_E0','logic_grammar.py',153),
  ('E -> B','E',1,'p_E1','logic_grammar.py',157),
  ('E -> N','E',1,'p_E1','logic_grammar.py',158),
  ('E -> string','E',1,'p_E1','logic_grammar.py',159),
  ('E -> ( E )','E',3,'p_E1','logic_grammar.py',160),
  ('E -> var ( arg_list )','E',4,'p_E2','logic_grammar.py',167),
  ('E -> var ( )','E',3,'p_E2','logic_grammar.py',168),
  ('var_list -> var','var_list',1,'p_var_list','logic_grammar.py',174),
  ('var_list -> var_list , var','var_list',3,'p_var_list','logic_grammar.py',175),
  ('args -> <empty>','args',0,'p_args','logic_grammar.py',185),
  ('args -> var_list','args',1,'p_args','logic_grammar.py',186),
]
