views:
  - title: Home
    theme: ios-dark-mode-dark-blue
    icon: ''
    badges: []
    cards:
      - type: vertical-stack
        cards:
          - type: iframe
            url: /local/clock/index.html
            aspect_ratio: 50%
          - type: entity
            entity: sensor.mi_2186809020_message
            state_color: true
            name: 消息
          - type: custom:mushroom-template-card
            primary: |2-
               {{ state_attr('weather.wo_de_jia', 'forecast_hourly') }}

            secondary: |2-
               {{ state_attr('weather.wo_de_jia', 'forecast_minutely') }}

            icon: mdi:weather-cloudy
          - type: custom:weather-card
            entity: weather.wo_de_jia
            details: true
            current: true
            forecast: true
            hourly_forecast: false
          - type: iframe
            url: >-
              https://embed.windy.com/embed2.html?lat=24.301&lon=109.435&detailLat=24.358&detailLon=109.435&width=650&height=450&zoom=11&level=surface&overlay=wind&product=ecmwf&menu=&message=&marker=true&calendar=now&pressure=true&type=map&location=coordinates&detail=true&metricWind=default&metricTemp=default&radarRange=-1
            aspect_ratio: 100%
      - type: vertical-stack
        cards:
          - type: picture-elements
            image: /local/house/wansh-0.png
            elements:
              - type: image
                entity: light.hyd_znlyj5_e153_light
                tap_action:
                  action: none
                style:
                  pointer-events: none
                  top: 50%
                  left: 50%
                  width: 100%
                  mix_blend_mode: lighten
                state_image:
                  'off': /local/house/touming.png
                  'on': /local/house/yangtai.png
              - type: state-icon
                entity: light.hyd_znlyj5_e153_light
                style:
                  top: 27%
                  left: 62%
                tap_action:
                  action: toggle
                icon: mdi:ceiling-light
              - type: image
                entity: light.yeelink_mbulb3_004f_light
                tap_action:
                  action: none
                style:
                  pointer-events: none
                  top: 63.5%
                  left: 21%
                  width: 36%
                  mix_blend_mode: lighten
                state_image:
                  'off': /local/house/touming.png
                  'on': /local/house/zhuwo.png
              - type: state-icon
                entity: light.yeelink_mbulb3_004f_light
                style:
                  top: 60%
                  left: 15%
                tap_action:
                  action: toggle
                icon: mdi:ceiling-light
              - type: image
                entity: light.yeelink_mbulb3_3884_light
                tap_action:
                  action: none
                style:
                  pointer-events: none
                  top: 50%
                  left: 50%
                  width: 100%
                  mix_blend_mode: lighten
                state_image:
                  'off': /local/house/touming.png
                  'on': /local/house/ciwo001.png
              - type: state-icon
                entity: light.yeelink_mbulb3_3884_light
                style:
                  top: 67%
                  left: 42%
                tap_action:
                  action: toggle
                icon: mdi:ceiling-light-multiple
              - type: image
                entity: switch.zimi_dhkg01_9672_switch
                tap_action:
                  action: none
                style:
                  pointer-events: none
                  top: 50%
                  left: 50%
                  width: 100%
                  mix_blend_mode: lighten
                state_image:
                  'off': /local/house/touming.png
                  'on': /local/house/keting.png
              - type: state-icon
                entity: switch.zimi_dhkg01_9672_switch
                style:
                  top: 70%
                  left: 80%
                tap_action:
                  action: toggle
                icon: mdi:chandelier
              - type: image
                entity: light.yeelink_mbulb3_38a7_light
                tap_action:
                  action: none
                style:
                  pointer-events: none
                  top: 72%
                  left: 59%
                  width: 19%
                  mix_blend_mode: lighten
                state_image:
                  'off': /local/house/touming.png
                  'on': /local/house/shufang.png
              - type: state-icon
                entity: light.yeelink_mbulb3_38a7_light
                style:
                  top: 70%
                  left: 55%
                tap_action:
                  action: toggle
                icon: mdi:ceiling-light
              - type: image
                entity: switch.zimi_dhkg05_8bb0_middle_switch_service
                tap_action:
                  action: none
                style:
                  pointer-events: none
                  top: 50%
                  left: 50%
                  width: 100%
                  mix_blend_mode: lighten
                state_image:
                  'off': /local/house/touming.png
                  'on': /local/house/zoulang.png
              - type: state-icon
                entity: switch.zimi_dhkg05_8bb0_middle_switch_service
                style:
                  top: 53%
                  left: 55%
                tap_action:
                  action: toggle
                icon: mdi:ceiling-light
              - type: image
                entity: switch.zimi_dhkg05_8bb0_right_switch_service
                tap_action:
                  action: none
                style:
                  pointer-events: none
                  top: 50%
                  left: 50%
                  width: 100%
                  mix_blend_mode: lighten
                state_image:
                  'off': /local/house/touming.png
                  'on': /local/house/weishengjian.png
              - type: state-icon
                entity: switch.zimi_dhkg05_8bb0_right_switch_service
                style:
                  top: 45%
                  left: 60%
                tap_action:
                  action: toggle
                icon: mdi:ceiling-light
          - type: horizontal-stack
            cards:
              - type: custom:mushroom-template-card
                primary: 亮灯
                secondary: >-
                  {{states.light | selectattr('state', 'eq', 'on') |
                  selectattr('attributes.friendly_name', 'search', '灯') | list |
                  count +

                  states.switch | selectattr('state', 'eq', 'on') |
                  selectattr('attributes.friendly_name', 'search', '灯') | list |
                  count}}
                icon: mdi:lightbulb
                icon_color: yellow
                tap_action:
                  action: call-service
                  service: xiaomi_miot.intelligent_speaker
                  target: {}
                  data:
                    execute: true
                    silent: true
                    throw: true
                    entity_id: media_player.xiaomi_l05c_009b_play_control
                    text: 关闭所有灯
                badge_color: ''
              - type: custom:mushroom-template-card
                primary: 空调
                secondary: >-
                  {{states.climate | rejectattr('state', 'eq', 'off') |
                  rejectattr('state', 'eq', 'unavailable') | list | count  }}
                icon: mdi:air-conditioner
                icon_color: green
                tap_action:
                  action: call-service
                  service: xiaomi_miot.intelligent_speaker
                  target: {}
                  data:
                    execute: true
                    silent: true
                    throw: true
                    entity_id: media_player.xiaomi_l05c_009b_play_control
                    text: 关闭所有空调
              - type: custom:mushroom-template-card
                primary: 风扇
                secondary: >-
                  {{states.fan | selectattr('state', 'eq', 'on') |
                  selectattr('attributes.friendly_name', 'search', '风扇') | list
                  | count }}
                icon: mdi:ceiling-fan
                icon_color: blue
                tap_action:
                  action: call-service
                  service: xiaomi_miot.intelligent_speaker
                  target: {}
                  data:
                    execute: true
                    entity_id: media_player.xiaomi_l05c_009b_play_control
                    text: 关闭所有风扇
                    silent: true
                    throw: true
          - square: false
            type: grid
            cards:
              - type: conditional
                conditions:
                  - condition: state
                    entity: light.yeelink_mbulb3_38a7_light
                    state: 'on'
                card:
                  type: custom:mushroom-chips-card
                  chips:
                    - type: light
                      entity: light.yeelink_mbulb3_38a7_light
                      content_info: name
                      name: 书房
                      use_light_color: true
              - type: conditional
                conditions:
                  - condition: state
                    entity: switch.zimi_dhkg01_9672_switch
                    state: 'on'
                card:
                  type: custom:mushroom-chips-card
                  chips:
                    - type: entity
                      entity: switch.zimi_dhkg01_9672_switch
                      icon_color: accent
                      icon: mdi:lightbulb
                      content_info: name
                      use_entity_picture: true
                      name: 客厅
              - type: conditional
                conditions:
                  - condition: state
                    entity: switch.zimi_dhkg05_8bb0_middle_switch_service
                    state: 'on'
                card:
                  type: custom:mushroom-chips-card
                  chips:
                    - type: entity
                      entity: switch.zimi_dhkg05_8bb0_middle_switch_service
                      icon_color: accent
                      icon: mdi:lightbulb
                      content_info: name
                      use_entity_picture: true
                      name: 走廊
              - type: conditional
                conditions:
                  - condition: state
                    entity: switch.zimi_dhkg05_8bb0_right_switch_service
                    state: 'on'
                card:
                  type: custom:mushroom-chips-card
                  chips:
                    - type: entity
                      entity: switch.zimi_dhkg05_8bb0_right_switch_service
                      icon_color: accent
                      icon: mdi:lightbulb
                      content_info: name
                      use_entity_picture: true
                      name: 卫生间
              - type: conditional
                conditions:
                  - condition: state
                    entity: fan.dmaker_p9_431d_fan
                    state: 'off'
                card:
                  type: custom:mushroom-chips-card
                  chips:
                    - type: entity
                      entity: fan.dmaker_p9_431d_fan
              - type: conditional
                conditions:
                  - condition: state
                    entity: light.hyd_znlyj5_e153_light
                    state: 'on'
                card:
                  type: custom:mushroom-chips-card
                  chips:
                    - type: light
                      entity: light.hyd_znlyj5_e153_light
                      icon: mdi:lightbulb
                      content_info: name
                      use_light_color: true
                      name: 阳台
              - type: conditional
                conditions:
                  - condition: numeric_state
                    entity: sensor.loock_s30_0629_battery_level
                    above: 0
                    below: 60
                card:
                  type: custom:mushroom-chips-card
                  chips:
                    - type: entity
                      entity: sensor.loock_s30_0629_battery_level
                      icon: mdi:door-closed-lock
              - type: conditional
                conditions:
                  - condition: numeric_state
                    entity: sensor.iphone_battery_level
                    above: 0
                    below: 30
                card:
                  type: custom:mushroom-chips-card
                  chips:
                    - type: entity
                      entity: sensor.iphone_battery_level
                      icon: mdi:cellphone
              - type: conditional
                conditions:
                  - condition: state
                    entity: light.yeelink_mbulb3_3884_light
                    state: ''
                card:
                  type: custom:mushroom-chips-card
                  chips:
                    - type: entity
                      entity: light.yeelink_mbulb3_3884_light
                      content_info: name
                      icon_color: accent
                      icon: mdi:alarm-light
                      name: 次卧
                      use_entity_picture: true
              - type: conditional
                conditions:
                  - condition: state
                    entity: light.yeelink_mbulb3_004f_light
                    state: 'on'
                card:
                  type: custom:mushroom-chips-card
                  chips:
                    - type: light
                      entity: light.yeelink_mbulb3_004f_light
                      use_light_color: true
                      content_info: name
                      name: 主卧
            columns: 6
          - type: media-control
            entity: media_player.xiaomi_l05c_009b_play_control
            theme: ios-dark-mode-blue-red
          - type: media-control
            entity: media_player.yun_yin_le
          - type: horizontal-stack
            cards:
              - type: custom:mushroom-template-card
                primary: 我的收藏
                secondary: ''
                icon: mdi:harddisk
                tap_action:
                  action: call-service
                  service: media_player.play_media
                  target:
                    device_id: 0c88f7d26a181b09bdc10dd60c7c7cbc
                  data:
                    media_content_id: cloudmusic://163/my/ilike
                    media_content_type: music
                badge_color: yellow
                icon_color: yellow
              - type: custom:mushroom-template-card
                primary: 每日推荐
                secondary: ''
                icon: mdi:music-circle
                tap_action:
                  action: call-service
                  service: media_player.play_media
                  target:
                    device_id: 0c88f7d26a181b09bdc10dd60c7c7cbc
                  data:
                    media_content_id: cloudmusic://163/my/daily
                    media_content_type: music
                icon_color: green
                badge_color: ''
          - type: horizontal-stack
            cards:
              - type: custom:mini-graph-card
                entities:
                  - entity: sensor.wo_de_jia_shi_du
                    name: 湿度
                    show_state: true
              - type: custom:mini-graph-card
                entities:
                  - entity: sensor.wo_de_jia_yu_liang
                    name: 降雨量
                    show_state: true
              - type: custom:mini-graph-card
                entities:
                  - entity: sensor.wo_de_jia_zi_wai_xian
                    name: 紫外线
                    show_state: true
          - type: custom:mini-graph-card
            entities:
              - sensor.wo_de_jia_wen_du
              - sensor.wo_de_jia_gan_jue_wen_du
              - sensor.wo_de_jia_feng_su
      - type: vertical-stack
        cards:
          - type: horizontal-stack
            cards:
              - type: custom:mushroom-person-card
                entity: person.leoleo
                icon_type: entity-picture
              - type: custom:mushroom-person-card
                entity: person.nu_wang
                icon_type: entity-picture
              - type: custom:mushroom-person-card
                entity: person.peng_yu_yan
                icon_type: entity-picture
          - type: horizontal-stack
            cards:
              - type: vertical-stack
                cards:
                  - type: entities
                    entities:
                      - entity: zone.home
                      - entity: sensor.iphone_battery_level
                      - entity: sensor.iphone_steps
                    footer:
                      type: graph
                      entity: sensor.iphone_battery_level
              - type: entities
                entities:
                  - entity: sensor.loock_s30_0629_battery_level
                    name: 鹿锁电量
                  - entity: sensor.loock_s30_0629_lock
                    name: 方式
                  - entity: sensor.loock_s30_0629_lock_action
                    name: 途径
                  - entity: sensor.loock_s30_0629_timestamp
                    name: 时间
          - square: true
            type: grid
            cards:
              - show_name: true
                show_icon: true
                type: button
                tap_action:
                  action: more-info
                show_state: true
                icon: mdi:television
                entity: media_player.miir_ir01_3170_ir_tv_control
                name: 电视
              - show_name: true
                show_icon: true
                type: button
                tap_action:
                  action: toggle
                entity: media_player.miir_ir01_6128_ir_projector_control
                show_state: false
                name: 坚果投影仪
              - show_name: true
                show_icon: true
                show_state: true
                entity: switch.minij_v8_f83c_switch_status
                icon: mdi:washing-machine
                name: 洗衣机
                type: button
                tap_action:
                  action: navigate
                  navigation_path: http://192.168.101.3:8123/dashboard-test/test?edit=1
              - show_name: true
                show_icon: true
                type: button
                tap_action:
                  action: call-service
                  service: xiaomi_miot.intelligent_speaker
                  target: {}
                  data:
                    execute: true
                    silent: true
                    throw: true
                    entity_id: media_player.xiaomi_l05c_009b_play_control
                    text: 播放因为
                entity: media_player.xiaomi_l05c_009b_play_control
                show_state: true
                name: 小爱同学
              - show_state: true
                show_name: true
                camera_view: auto
                type: picture-entity
                entity: switch.zimi_dhkg01_9672_switch
                image: https://demo.home-assistant.io/stub_config/bedroom.png
                aspect_ratio: 150%
                tap_action:
                  action: toggle
                name: 客厅
              - show_name: true
                show_icon: true
                type: button
                tap_action:
                  action: toggle
                entity: light.hyd_znlyj5_e153_light
                name: 阳台
              - show_name: true
                show_icon: true
                type: button
                tap_action:
                  action: toggle
                entity: switch.zimi_dhkg05_8bb0_middle_switch_service
                icon: mdi:lightbulb
              - show_name: true
                show_icon: true
                type: button
                tap_action:
                  action: toggle
                entity: switch.zimi_dhkg05_8bb0_right_switch_service
                icon: mdi:lightbulb
            columns: 4
          - square: false
            type: grid
            cards:
              - type: custom:mushroom-light-card
                entity: light.yeelink_mbulb3_004f_light
                layout: horizontal
                use_light_color: true
                show_color_temp_control: true
                collapsible_controls: true
                show_color_control: true
                show_brightness_control: true
                icon_color: primary
              - type: custom:mushroom-light-card
                entity: light.yeelink_mbulb3_38a7_light
                layout: horizontal
                show_brightness_control: true
                show_color_control: true
                show_color_temp_control: true
                use_light_color: true
                collapsible_controls: true
              - type: custom:mushroom-fan-card
                entity: fan.dmaker_p9_431d_fan
                icon_animation: true
                show_percentage_control: true
                layout: horizontal
                show_oscillate_control: true
                collapsible_controls: true
              - type: custom:mushroom-climate-card
                entity: climate.miir_ir02_7712_ir_aircondition_control
                hold_action:
                  action: more-info
              - type: custom:mushroom-climate-card
                entity: climate.lumi_mcn02_0a06_air_conditioner
                hold_action:
                  action: more-info
              - type: custom:mushroom-climate-card
                entity: climate.lumi_mcn02_aee4_air_conditioner
                hold_action:
                  action: more-info
            columns: 1
          - type: entities
            entities:
              - sensor.sun_next_dawn
              - sensor.sun_next_dusk
              - sensor.sun_next_midnight
  - title: 洗衣机页面
    path: test
    icon: mdi:washing-machine
    subview: true
    theme: ios-dark-mode-dark-blue
    badges: []
    cards:
      - type: entities
        entities:
          - entity: button.minij_v8_f83c_start_wash
            name: 开始洗衣
          - entity: sensor.minij_v8_f83c_washer
            name: 当前状态
          - entity: switch.minij_v8_f83c_washer_status
          - entity: select.minij_v8_f83c_mode
            name: 选择模式
          - entity: select.minij_v8_f83c_rinsh_times
          - entity: select.minij_v8_f83c_drying_level
            name: 干燥温度
          - entity: select.minij_v8_f83c_spin_speed
            name: 转速
          - entity: select.minij_v8_f83c_target_temperature
            name: 水温
          - entity: select.minij_v8_f83c_target_water_level
            name: 水位
        title: 洗衣机
        header:
          type: picture
          image: >-
            https://www.home-assistant.io/images/lovelace/header-footer/balloons-header.png
          tap_action:
            action: none
          hold_action:
            action: none
  - title: dianshi
    path: dianshi
    badges: []
    cards:
      - type: entities
        entities:
          - entity: switch.magic_switch_s1e_14bb_switch_1
            name: Switch 1
          - entity: switch.magic_switch_s1e_14bb_switch_2
            name: Switch 2
          - entity: switch.magic_switch_s1e_14bb_switch_3
            name: Switch 3
        title: Magic-Switch-S1E-14BB
      - type: entities
        entities:
          - entity: event.magic_switch_s1e_14bb_button_1
            name: Button 1
          - entity: event.magic_switch_s1e_14bb_button_2
            name: Button 2
          - entity: event.magic_switch_s1e_14bb_button_3
            name: Button 3
          - entity: event.magic_switch_s1e_14bb_button_4
            name: Button 4
          - entity: event.magic_switch_s1e_14bb_button_5
            name: Button 5
          - entity: event.magic_switch_s1e_14bb_button_6
            name: Button 6
        title: Magic-Switch-S1E-14BB
      - type: media-control
        entity: media_player.yun_yin_le
      - type: grid
        square: false
        columns: 1
        cards:
          - type: entities
            entities:
              - entity: light.c949e1af_5a8e8d82_screen
                name: Screen
            title: c949e1af-5a8e8d82
          - type: media-control
            entity: media_player.c949e1af_5a8e8d82
  - title: xxx
    path: xxx
    type: panel
    badges: []
    cards:
      - type: picture-elements
        image: /local/phone/myhome001.png
        elements:
          - type: image
            entity: light.hyd_znlyj5_e153_light
            tap_action:
              action: none
            style:
              pointer-events: none
              top: 50%
              left: 50.5%
              width: 100%
              mix_blend_mode: lighten
            state_image:
              'off': /local/house/touming.png
              'on': /local/phone/yangtai.png
          - type: state-icon
            entity: light.hyd_znlyj5_e153_light
            style:
              top: 27%
              left: 65%
            tap_action:
              action: toggle
            icon: mdi:ceiling-light
          - type: image
            entity: light.yeelink_mbulb3_004f_light
            tap_action:
              action: none
            style:
              pointer-events: none
              top: 50%
              left: 50.5%
              width: 100%
              mix_blend_mode: lighten
            state_image:
              'off': /local/house/touming.png
              'on': /local/phone/zhuwo.png
          - type: state-icon
            entity: light.yeelink_mbulb3_004f_light
            style:
              top: 60%
              left: 35%
            tap_action:
              action: toggle
            icon: mdi:ceiling-light
          - type: image
            entity: light.yeelink_mbulb3_3884_light
            tap_action:
              action: none
            style:
              pointer-events: none
              top: 50%
              left: 50.5%
              width: 100%
              mix_blend_mode: lighten
            state_image:
              'off': /local/house/touming.png
              'on': /local/phone/ciwo.png
          - type: state-icon
            entity: light.yeelink_mbulb3_3884_light
            style:
              top: 67%
              left: 52%
            tap_action:
              action: toggle
            icon: mdi:ceiling-light-multiple
          - type: image
            entity: switch.zimi_dhkg01_9672_switch
            tap_action:
              action: none
            style:
              pointer-events: none
              top: 50%
              left: 50.5%
              width: 100%
              mix_blend_mode: lighten
            state_image:
              'off': /local/house/touming.png
              'on': /local/phone/keting.png
          - type: state-icon
            entity: switch.zimi_dhkg01_9672_switch
            style:
              top: 70%
              left: 80%
            tap_action:
              action: toggle
            icon: mdi:chandelier
          - type: image
            entity: light.yeelink_mbulb3_38a7_light
            tap_action:
              action: none
            style:
              pointer-events: none
              top: 50%
              left: 50.5%
              width: 100%
              mix_blend_mode: lighten
            state_image:
              'off': /local/house/touming.png
              'on': /local/phone/shufang.png
          - type: state-icon
            entity: light.yeelink_mbulb3_38a7_light
            style:
              top: 70%
              left: 65%
            tap_action:
              action: toggle
            icon: mdi:ceiling-light
          - type: image
            entity: switch.zimi_dhkg05_8bb0_middle_switch_service
            tap_action:
              action: none
            style:
              pointer-events: none
              top: 50%
              left: 50.5%
              width: 100%
              mix_blend_mode: lighten
            state_image:
              'off': /local/house/touming.png
              'on': /local/phone/zoulang.png
          - type: state-icon
            entity: switch.zimi_dhkg05_8bb0_middle_switch_service
            style:
              top: 53%
              left: 60%
            tap_action:
              action: toggle
            icon: mdi:ceiling-light
          - type: image
            entity: switch.zimi_dhkg05_8bb0_right_switch_service
            tap_action:
              action: none
            style:
              pointer-events: none
              top: 50%
              left: 50.5%
              width: 100%
              mix_blend_mode: lighten
            state_image:
              'off': /local/house/touming.png
              'on': /local/phone/weishengjian.png
          - type: state-icon
            entity: switch.zimi_dhkg05_8bb0_right_switch_service
            style:
              top: 42%
              left: 65%
            tap_action:
              action: toggle
            icon: mdi:ceiling-light
title: Liao‘s Home
