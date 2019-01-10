select 
( SELECT GLCAT_MCAT_ID FROM PC_ITEM_TO_GLCAT_MCAT, GLCAT_MCAT WHERE FK_PC_ITEM_ID = PC_ITEM_ID AND ITEM_MAPPING_ISPRIME = -1 AND GLCAT_MCAT_ID = FK_GLCAT_MCAT_ID ) PRIME_MCAT_ID,
( SELECT GLCAT_MCAT_IS_GENERIC FROM PC_ITEM_TO_GLCAT_MCAT, GLCAT_MCAT WHERE FK_PC_ITEM_ID = PC_ITEM_ID AND ITEM_MAPPING_ISPRIME = -1 AND GLCAT_MCAT_ID = FK_GLCAT_MCAT_ID ) PRIME_MCAT_IS_GENERIC,
( SELECT FK_MCAT_TYPE_ID FROM PC_ITEM_TO_GLCAT_MCAT, GLCAT_MCAT WHERE FK_PC_ITEM_ID = PC_ITEM_ID AND ITEM_MAPPING_ISPRIME = -1 AND GLCAT_MCAT_ID = FK_GLCAT_MCAT_ID ) FK_MCAT_TYPE_ID,
( SELECT GLCAT_MCAT_NAME FROM PC_ITEM_TO_GLCAT_MCAT, GLCAT_MCAT WHERE FK_PC_ITEM_ID = PC_ITEM_ID AND ITEM_MAPPING_ISPRIME = -1 AND GLCAT_MCAT_ID = FK_GLCAT_MCAT_ID ) PRIME_MCAT_NAME,
( SELECT WM_CONCAT(GLCAT_MCAT_NAME) FROM PC_ITEM_TO_GLCAT_MCAT, GLCAT_MCAT WHERE FK_PC_ITEM_ID = PC_ITEM_ID AND NVL(ITEM_MAPPING_ISPRIME,0) <> -1 AND GLCAT_MCAT_ID = FK_GLCAT_MCAT_ID ) OTHER_MCATS,
pc_item_to_glcat_mcat.FK_GLCAT_MCAT_ID,PC_ITEM_ID,PC_ITEM_NAME ,PC_ITEM_IMG_ORIGINAL, PC_ITEM_GLUSR_USR_ID, PC_ITEM_GLCAT_MCAT_ID_LIST, PC_ITEM_GLCAT_MCAT_NAME_LIST,pc_item.PC_ITEM_STATUS_APPROVAL ,pc_item.PC_ITEM_DESC_SMALL ,
FK_IM_SPEC_MASTER_ID, FK_IM_SPEC_MASTER_DESC,FK_IM_SPEC_OPTIONS_ID, FK_IM_SPEC_OPTIONS_DESC,PC_ITEM_ATTRIBUTE_MCATID "Response MCAT",PC_ITEM_ATTRIBUTE_MOD_DATE,fk_glcat_mcat_id "Current MCAT"
from pc_item
left join pc_item_to_glcat_mcat
on (pc_item_to_glcat_mcat.fk_pc_item_id=pc_item.pc_item_id)
left join PC_ITEM_ATTRIBUTE
on (PC_ITEM_ATTRIBUTE.FK_PC_ITEM_ID=pc_item_to_glcat_mcat.fk_pc_item_id )
where fk_glcat_mcat_id in (22752,
194569,
77603,
194319,
194340,
105093,
27188,
6781,
73184,
194570,
113951,
178569,
134099,
37924,
194309,
194577,
203197,
193423,
41181,
194708,
194695,
142260,
26925,
204269,
193902,
193203,
194684,
165949,
177690,
126618,
39496,
194968,
136851,
207385,
121250,
206686,
193228,
188783,
193391,
206688,
193995,
193202,
193201,
193994,
181819,
206690,
193426,
206687,
206689,
193227,
193244,
193420,
206691,
193345,
191243,
193370,
203531,
206710,
204879,
193369,
206713,
206712,
193422,
206711,
159664,
203647,
203650,
206703,
49800,
206708,
206709,
203648,
206706,
184296,
193373,
203649,
204878,
193210,
204877,
206707,
204876,
206272,
206704,
206705,
207955,
193421,
193346,
174274,
188314,
188315,
68051,
22751,
65574,
65575,
164422,
142259,
164423,
106197,
190843,
114204,
159749,
183008,
163436,
151413,
167743,
164435,
179196,
84514,
68058,
88369,
194704,
194677,
33075,
161621,
114132,
37742,
185530,
194721,
206701,
186441,
179224,
173861,
193200,
200099,
73183,
193316,
206055,
204875,
204874,
206700,
142555,
185716,
191802,
68056,
68057,
164425,
188626,
142261,
183990,
142262,
164497,
113923,
164496,
190117,
87633,
204982,
177935,
206680,
206679,
193344,
193315,
68053,
206675,
193000,
68054,
206681,
109988,
182638,
15607,
189739,
180381,
193001,
189386,
205104,
191154,
206676,
206674,
193238,
206677,
32778,
185100,
35526,
206682,
193235,
206684,
191144,
193418,
193304,
184967,
206685,
193058,
206683,
206678,
193852,
206692,
193204,
204450,
206695,
206698,
206693,
193229,
206694,
204449,
204873,
164434,
175968,
204872,
206237,
206696,
206697,
204871,
194928,
193317,
68052,
42684,
68057,
142263,
155897,
142264,
189132,
138404,
142366)
and pc_item_id is not null
order by PC_ITEM_ATTRIBUTE_MCATID,FK_IM_SPEC_MASTER_ID,FK_IM_SPEC_OPTIONS_ID,pc_item_id;