#coding=utf-8
#author: wwj718
#author_email: wuwenjie718@gmail.com
#author_blog: wwj718.github.io

""" sewiseXBlock main Python class"""

import pkg_resources
from django.template import Context, Template

from xblock.core import XBlock
from xblock.fields import Scope, Integer, String, Boolean
from xblock.fragment import Fragment
import requests
class sewiseXBlock(XBlock):

    '''
    Icon of the XBlock. Values : [other (default), video, problem]
    '''
    icon_class = "video"

    '''
    Fields
    '''
    display_name = String(display_name="Display Name",
        default="sewise player",
        scope=Scope.settings,
        help="This name appears in the horizontal navigation at the top of the page.")


    app_id = String(display_name="video client_id",
	default="sewise",
	scope=Scope.content, #Scope.content和Scope.settings不同在于，(可见性)本课多处可用
	help="The  client_id for your video.")

    video_id = String(display_name="video vid",
	default="sewise",
	scope=Scope.content, #Scope.content和Scope.settings不同在于，(可见性)本课多处可用
	help="The vid for your video.")


    width = Integer(display_name="Video player width",
	default="560",
	scope=Scope.content,
	help="The width for your video player.")
    height = Integer(display_name="Video player height",
	default="320",
	scope=Scope.content,
	help="The height for your video player.")

    '''
    Util functions
    '''
    def load_resource(self, resource_path):
        """
        Gets the content of a resource
        """
        resource_content = pkg_resources.resource_string(__name__, resource_path)
        return unicode(resource_content)

    def render_template(self, template_path, context={}):
        """
        Evaluate a template by resource path, applying the provided context
        """
        template_str = self.load_resource(template_path)
        return Template(template_str).render(Context(context))

    '''
    Main functions
    '''
    def student_view(self, context=None):
        """
        The primary view of the XBlock, shown to students
        when viewing courses.
        """
        '''
	    #添加字段记录上回播放时间，应该是用户级别的
	    if self.start_time != "" and self.end_time != "":
            fullUrl += "#t=" + self.start_time + "," + self.end_time
        elif self.start_time != "":
            fullUrl += "#t=" + self.start_time
        elif self.end_time != "":
            fullUrl += "#t=0," + self.end_time
        '''
        context = {
            'display_name': self.display_name,
            'app_id' : self.app_id,
            'video_id': self.video_id,
            'width': self.width,
            'height': self.height
        }
        html = self.render_template('static/html/sewise_view.html', context)
        frag = Fragment(html)
        #frag.add_javascript(self.load_resource('static/js/h5connect.js')) #内有中文，使用插入外部url
        #frag.add_javascript(self.load_resource("static/js/sewise.player.min.js"))
        frag.add_javascript(self.load_resource("static/js/sewise_view.js"))
        frag.initialize_js('sewiseXBlockInitView')
        return frag

    def studio_view(self, context=None):
        """
        The secondary view of the XBlock, shown to teachers
        when editing the XBlock.
        """
        context = {
            'display_name': self.display_name,
            'app_id' : self.app_id,
            'video_id': self.video_id,
            'width': self.width,
            'height': self.height
        }
        html = self.render_template('static/html/sewise_edit.html', context)

        frag = Fragment(html)
        frag.add_javascript(self.load_resource("static/js/sewise_edit.js"))
        frag.initialize_js('sewiseXBlockInitStudio')
        return frag

    @XBlock.json_handler
    def save_sewise(self, data, suffix=''):
        """
        The saving handler.
        """
        self.display_name = data['display_name']
        self.video_id = data['video_id']
        self.width = data['width']
        self.height = data['height']

        return {
            'result': 'success',
        }

    @XBlock.json_handler
    def get_params(self, data, suffix=''):
        '''called when sewise init'''
        #sessionid = "7f299b0c2d89269f20c9eca2c2b637b6"
        sessionid = data["sessionid"]
        base_url = "http://videoapi.unihse.com:8888/video/player/"
        url = base_url+self.video_id+"/"+sessionid
        response = requests.get(url)
        response_json = response.json()
        return {
                "data":response_json,
                "sessionid":data,
                }

    @staticmethod
    def workbench_scenarios():
        return [
              ("sewise demo", "<sewise />")  #the name should be "<sewise />"
        ]
