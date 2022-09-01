import unittest

from kyu5.poohbear_lang import poohbear


class PoohbearLangTests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(poohbear('LQTcQAP>pQBBTAI-PA-PPL+P<BVPAL+T+P>PL+PBLPBP<DLLLT+P'), 'Hello World!')

    def test_2(self):
        self.assertEqual(poohbear('LLQT+P >LLLc+QIT-P AAAP P'), '!]oo')

    def test_3(self):
        self.assertEqual(poohbear('LLQT>+WN+<P>E'),
                         '1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106 107 108 109 110 111 112 113 114 115 116 117 118 119 120 121 122 123 124 125 126 127 128 129 130 131 132 133 134 135 136 137 138 139 140 141 142 143 144 145 146 147 148 149 150 151 152 153 154 155 156 157 158 159 160 161 162 163 164 165 166 167 168 169 170 171 172 173 174 175 176 177 178 179 180 181 182 183 184 185 186 187 188 189 190 191 192 193 194 195 196 197 198 199 200 201 202 203 204 205 206 207 208 209 210 211 212 213 214 215 216 217 218 219 220 221 222 223 224 225 226 227 228 229 230 231 232 233 234 235 236 237 238 239 240 241 242 243 244 245 246 247 248 249 250 251 252 253 254 255 ')

    def test_4(self):
        self.assertEqual(poohbear('cW>LQQT+P<pE'), '')

    def test_5(self):
        self.assertEqual(poohbear('+W>LQQT+P<-E'), '!')

    def test_6(self):
        self.assertEqual(poohbear('+LTQII>+WN<P>+E'),
                         '1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106 107 108 109 110 111 112 113 114 115 116 117 118 119 120 121 122 123 124 125 126 127 128 129 130 131 132 133 134 135 136 137 138 139 140 141 142 143 144 145 146 147 148 149 150 151 152 153 154 155 156 157 158 159 160 161 162 163 164 165 166 167 168 169 170 171 172 173 174 175 176 177 178 179 180 181 182 183 184 185 186 187 188 189 190 191 192 193 194 195 196 197 198 199 200 201 202 203 204 205 206 207 208 209 210 211 212 213 214 215 216 217 218 219 220 221 222 223 224 225 226 227 228 229 230 231 232 233 234 235 236 237 238 239 240 241 242 243 244 245 246 247 248 249 250 251 252 253 254 255 ')

    def test_7(self):
        self.assertEqual(poohbear('+LTQIITTIWP-E'),
                         '~}|{zyxwvutsrqponmlkjihgfedcba`_^]\\[ZYXWVUTSRQPONMLKJIHGFEDCBA@?>=<;:9876543210/.-,+*)(\'&%$#"! \x1f\x1e\x1d\x1c\x1b\x1a\x19\x18\x17\x16\x15\x14\x13\x12\x11\x10\x0f\x0e\r\x0c\x0b\n\t\x08\x07\x06\x05\x04\x03\x02\x01')

    def test_8(self):
        self.assertEqual(poohbear('LILcABNBpYDYYYYLLL+P-+W-EQNW-ELLQUTTTT+P'), "2'0A")

    def test_9(self):
        self.assertEqual(poohbear('++W-NE'), '10')

    def test_10(self):
        self.assertEqual(poohbear('W>UQLIPNPPP45vSDFJLLIPNPqwVMT<E'), '')

    def test_11(self):
        self.assertEqual(poohbear('LLILQQLcYYD'), '')

    def test_12(self):
        self.assertEqual(poohbear('NNN++-NTTTTT+PN'), '0001!33')

    def test_13(self):
        self.assertEqual(poohbear('LQQT+P+P+P+P+P+P'), '!"#$%&')

    def test_14(self):
        self.assertEqual(poohbear('+-<>LcIpIL+TQYDABANPAPIIIITUNNQV+++P'), '38&(88#')

    def test_15(self):
        self.assertEqual(poohbear('+c BANANA BANANA BANANA BANANA BANANA'), '12345678910')

    def test_16(self):
        self.assertEqual(poohbear(
            'L       sfdg           ghjk                         kl                                LQTT++++P                        tt                                W                  w                    -                                      E           wewewe                N'),
            'D0')


if __name__ == '__main__':
    unittest.main()
