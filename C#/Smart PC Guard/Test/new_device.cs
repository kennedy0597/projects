using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Management;
using InTheHand.Net.Sockets;
using System.Diagnostics;
using System.IO;




namespace Test
{
    public partial class new_device : Form
    {

        public string ReturnText { get; set; }
        public new_device()
        {
            InitializeComponent();
           

        }


        private void New_device_Load(object sender, EventArgs e)
        {

        }

        
        //Usb Device
        private void Button1_Click(object sender, EventArgs e)
        {
            foreach (System.IO.DriveInfo drive in System.IO.DriveInfo.GetDrives())
            {
                if ((drive.DriveType == System.IO.DriveType.Removable))
                {
                    checkedListBox2.Items.Add(drive.Name);
                }
            }
        }

   

        private void CheckedListBox2_SelectedIndexChanged(object sender, EventArgs e)
        {

        }

        private void CheckedListBox3_SelectedIndexChanged(object sender, EventArgs e)
        {
            
        }
        
      

        private void CheckedListBox1_SelectedIndexChanged(object sender, EventArgs e)
        {

        }

        private void CheckedListBox1_SelectedIndexChanged_1(object sender, EventArgs e)
        {

        }

        private void Button4_Click(object sender, DataReceivedEventArgs e)
        {
           
        }

        private void TextBox1_TextChanged(object sender, EventArgs e)
        {

        }

        public string UsbDevice { get; set; }
        private void Button4_Click(object sender, EventArgs e)
        {

            foreach (object itemChecked in checkedListBox2.CheckedItems)
            {
                
                this.ReturnText = this.textBox1.Text;
                textBox1.Text += itemChecked.ToString();
                UsbDevice = itemChecked.ToString();
             
            }
            
            
        }

        

        private void Button2_Click(object sender, EventArgs e)
        {
            foreach (DriveInfo drive in DriveInfo.GetDrives())
            {
                if (drive.Name == UsbDevice)
                {
                    DirectoryInfo dir = new DirectoryInfo(drive.Name + "/locker");
                    dir.CreateSubdirectory("Test");
                    FileInfo fi = new FileInfo(drive.Name + @"locker/locker.txt");
                    StreamWriter SW = fi.CreateText();
                    SW.WriteLine("abc");
                    SW.Close();

                    MessageBox.Show("key added");
                    this.Close();

                    Main ss = new Main(textBox1.Text);
                    ss.Show();
                }
            }
           
            
            
        }
        
        private void Button3_Click(object sender, EventArgs e)
        {
            Main main = new Main();
            main.Show();
            this.Close();
        }
    }
    
}

 
    

