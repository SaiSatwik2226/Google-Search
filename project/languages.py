s = """1	Mandarin	935 (955)	14.1%
2	Spanish	390 (405)	5.85%
3	English	365 (360)	5.52%
4	Hindi	295 (310)	4.46%
5	Arabic	280 (295)	4.23%
6	Portuguese	205 (215)	3.08%
7	Bengali	200 (205)	3.05%
8	Russian	160 (155)	2.42%
9	Japanese	125 (125)	1.92%
10	Punjabi	95 (100)	1.44%
11	German	92 (95)	1.39%
12	Javanese	82	1.25%
13	Wu	80	1.20%
14	Malay	77	1.16%
15	Telugu	76	1.15%
16	Vietnamese	76	1.14%
17	Korean	76	1.14%
18	French	75	1.12%
19	Marathi	73	1.10%
20	Tamil	70	1.06%
21	Urdu	66	0.99%
22	Turkish	63	0.95%
23	Italian	59	0.90%
24	Yue	59	0.89%
25	Thai	56	0.85%
26	Gujarati	49	0.74%
27	Jin	48	0.72%
28	Southern Min	47	0.71%
29	Persian	45	0.68%
30	Polish	40	0.61%
31	Pashto	39	0.58%
32	Kannada	38	0.58%
33	Xiang	38	0.58%
34	Malayalam	38	0.57%
35	Sundanese	38	0.57%
36	Hausa	34	0.52%
37	Odia	33	0.50%
38	Burmese	33	0.50%
39	Hakka	31	0.46%
40	Ukrainian	30	0.46%
41	Bhojpuri	29[b]	0.43%
42	Tagalog	28	0.42%
43	Yoruba	28	0.42%
44	Maithili	27[b]	0.41%
45	Uzbek	26	0.39%
46	Sindhi	26	0.39%
47	Amharic	25	0.37%
48	Fula	24	0.37%
49	Romanian	24	0.37%
50	Oromo	24	0.36%
51	Igbo	24	0.36%
52	Azerbaijani	23	0.34%
53	Awadhi	0.33%
54	Gan	22	0.33%
55	Cebuano	21	0.32%
56	Dutch	21	0.32%
57	Kurdish	21	0.31%
58	Serbo-Croatian	19	0.28%
59	Malagasy	18	0.28%
60	Saraiki	0.26%
61	Nepali	17	0.25%
62	Sinhala	16	0.25%
63	Chittagonian	16	0.24%
64	Zhuang	16	0.24%
65	Khmer	16	0.24%
66	Turkmen	16	0.24%
67	Assamese	15	0.23%
68	Madurese	15	0.23%
69	Somali	15	0.22%
70	Marwari	0.21%
71	Magahi	0.21%
72	Haryanvi	0.21%
73	Hungarian	13	0.19%
74	Chhattisgarhi	0.19%
75	Greek	12	0.18%
76	Chewa	12	0.17%
77	Deccan	11	0.17%
78	Akan	11	0.17%
79	Kazakh	11	0.17%
80	Northern Min	10.9	0.16%
81	Sylheti	10.7	0.16%
82	Zulu	10.4	0.16%
83	Czech	10.0	0.15%
84	Kinyarwanda	9.8	0.15%
85	Dhundhari	0.15%
86	Haitian Creole	9.6	0.15%
87	Eastern Min	9.5	0.14%
88	Ilocano	9.1	0.14%
89	Quechua	8.9	0.13%
90	Kirundi	8.8	0.13%
91	Swedish	8.7	0.13%
92	Hmong	8.4	0.13%
93	Shona	8.3	0.13%
94	Uyghur	8.2	0.12%
95	Hiligaynon/Ilonggo	8.2	0.12%
96	Mossi	7.6	0.11%
97	Xhosa	7.6	0.11%
98	Belarusian	7.6[d]	0.11%
99	Balochi	7.6	0.11%
100	Konkani	7.4	0.11%"""
li = s.split('\n')
nli = []

for i in li:
    t = (i.split('\t'))
    nli.append(t[1])


for i in nli:
    print("<option value=\""+i+"\""+">"+i+"</option>")

