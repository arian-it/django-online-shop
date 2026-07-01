import ghasedak_sms

sms_api = ghasedak_sms.Ghasedak('e446792bee2052994fea1bf7e680717bcd911a8485cdcf4c7240a84e2f4ea55cjthvB8rGeGB8ac3N')

def send_sms(phone, randcode):
    newotpcommand = ghasedak_sms.SendOtpInput(
        send_date=None,
        receptors=[
            ghasedak_sms.SendOtpReceptorDto(
                mobile=f'{phone}'
            )
        ],
        template_name='Ghasedak',
        inputs=[
            ghasedak_sms.SendOtpInput.OtpInput(param='Code', value=f'{randcode}'),
        ],
        udh=False
    )
    # response = sms_api.send_otp_sms(newotpcommand)

