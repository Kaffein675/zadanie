class Core:
    @staticmethod
    def core_devise(f_p, n, i, ksi, flag):
        if flag:
            u1 = f_p[i - 3]
            u2 = f_p[i - 2]
            u3 = f_p[i - 1]
            u4 = f_p[i]
            u5 = f_p[i + 1]
            u6 = f_p[i + 2]
        else:
            u6 = f_p[i - 2]
            u5 = f_p[i - 1]
            u4 = f_p[i]
            u3 = f_p[i + 1]
            u2 = f_p[i + 2]
            u1 = f_p[i + 3]
        s1 = u4 + ksi*ksi*ksi * (-u1 / 6. + u2 / 2. - u3 / 2. + u4 / 6.) + ksi*ksi * (-u1 / 2. + 2. * u2 - 5. * u3 / 2. + u4) + ksi*(-u1 / 3. + 3. * u2 / 2. - 3. * u3 + 11. * u4 / 6.)
        s2 = u4 + ksi*ksi*ksi * (-u2 / 6. + u3 / 2. - u4 / 2. + u5 / 6.) + ksi*ksi * (u3 / 2. - u4 + u5 / 2.) + ksi*(u2 / 6. - u3 + u4 / 2. + u5 / 3.)
        s3 = u4 + ksi*ksi*ksi * (-u3 / 6. + u4 / 2. - u5 / 2. + u6 / 6.) + ksi*ksi * (u3 / 2. - u4 + u5 / 2.) + ksi*(-u3 / 3. - u4 / 2. + u5 - u6 / 6.)
        c1 = (ksi - 1.)*(ksi - 2.) / 20.
        c2 = -(ksi + 3.)*(ksi - 2.) / 10.
        c3 = (ksi + 3.)*(ksi + 2.) / 20.
        beta1 = 4.*u1*u1 / 3. - 9.*u1*u2 + 10.*u1*u3 - 11. * u1*u4 / 3. + 16.*u2*u2 - 37.*u2*u3 + 14.*u2*u4 + 22.*u3*u3 - 17.*u3*u4 + 10.*u4*u4 / 3.
        beta2 = 4.*u2*u2 / 3. - 7.*u2*u3 + 6.*u2*u4 - 5.*u2*u5 / 3. + 10.*u3*u3 - 19.*u3*u4 + 6.*u3*u5 + 10.*u4*u4 - 7.* u4*u5 + 4.*u5*u5 / 3.
        beta3 = 10.*u3*u3 / 3. - 17.*u3*u4 + 14.*u3*u5 - 11.*u3*u6 / 3. + 22.*u4*u4 - 37.*u4*u5 + 10.*u4*u6 + 16.*u5*u5 - 9.*u5*u6 + 4.*u6*u6 / 3.
        eps = 1.0E-10
        wt1 = c1 / (eps + beta1) / (eps + beta1)
        wt2 = c2 / (eps + beta2) / (eps + beta2)
        wt3 = c3 / (eps + beta3) / (eps + beta3)
        w1 = wt1 / (wt1 + wt2 + wt3)
        w2 = wt2 / (wt1 + wt2 + wt3)
        w3 = wt3 / (wt1 + wt2 + wt3)
        return w1*s1 + w2*s2 + w3*s3
