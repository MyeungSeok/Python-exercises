'''
난수 생성기를 이용하여 안전한 비밀번호를 추천해 주시오.
옵션 :: 비밀번호의 길이/ 특수문자의 개수 / 대문자 개수 / 소문자 개수 / 숫자 개수
'''
from random import choice, sample


class RandomPasswordGenerator():

    sc_list = "~!@#$%^&*+=?"
    uc_list = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lc_list = "abcdefghijklmnopqrstuvwxyz"
    digit_list = "0123456789"
    all_list = sc_list + uc_list + lc_list + digit_list

    def __init__(self, length=4, num_sc=0, num_uc=0, num_lc=0, num_digit=0):
        self.length = length  # default: 4
        self.num_sc = num_sc
        self.num_uc = num_uc
        self.num_lc = num_lc
        self.num_digit = num_digit
        self.option_length = \
            self.num_sc + self.num_uc + self.num_lc + self.num_digit
        # 인자 검사
        self.check_args()

    def check_args(self):
        # 옵션값이 음수이면 에러 처리
        if (self.num_sc or self.num_uc or self.num_lc or self.num_digit) < 0:
            raise ValueError("generate()의 인자는 양의 정수여야 합니다.")
        # 옵션길이가 length보다 크면 에러 처리
        if self.length < self.option_length:
            raise ValueError("첫번째 인자 length는 나머지 인자들의 합과 같아야 합니다.")

    def generate(self):
        sc = ''.join(choice(self.sc_list) for i in range(self.num_sc))
        uc = ''.join(choice(self.uc_list) for i in range(self.num_uc))
        lc = ''.join(choice(self.lc_list) for i in range(self.num_lc))
        digit = ''.join(
            choice(self.digit_list) for i in range(self.num_digit)
        )
        remains_length = self.length-self.option_length
        remains = ''.join(choice(self.all_list) for i in range(remains_length))
        # 패스워드의 재료
        pw_source = sc + uc + lc + digit + remains
        # 재료들을 shuffle 하여 return
        return ''.join(sample(pw_source, len(pw_source)))


if __name__ == '__main__':
    # 길이, 특수문자, 대문자, 소문자, 숫자
    generator = RandomPasswordGenerator(8, 0, 4, 1, 3)
    password = generator.generate()
    print("생성된 패스워드: {}".format(password))
